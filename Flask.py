from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import secrets

app = Flask(__name__, template_folder='templates')
app.secret_key = secrets.token_hex(32)

# 🔐 Vérification des identifiants
def check_login(username, password):
    try:
        conn = sqlite3.connect('ecole.db')
        cursor = conn.cursor()
        cursor.execute("SELECT Role FROM users WHERE Identifiant = ? AND Mot_de_passe = ?", (username, password))
        user = cursor.fetchone()
        conn.close()
        return user[0] if user else None
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None

# 🏫 Tableau des notes pour professeurs
@app.route('/tableau_prof')
def tableau_prof():
    if 'username' not in session or session['role'] != 'prof':
        return redirect(url_for('login_form'))

    try:
        conn = sqlite3.connect("ecole.db")
        cursor = conn.cursor()

        cursor.execute("SELECT Identifiant, Nom, Prenom FROM users WHERE Role = 'eleve'")
        eleves = cursor.fetchall()

        cursor.execute("""
            SELECT u.Identifiant, u.Nom, u.Prenom, n.Trimestre, n.Matiere, n.note
            FROM users u 
            LEFT JOIN notes n ON u.Identifiant = n.Identifiant 
            WHERE u.Role = 'eleve'
            ORDER BY u.Identifiant, n.Trimestre
        """)
        eleves_notes = cursor.fetchall()

        conn.close()
        return render_template('TableauProf.html', eleves_notes=eleves_notes, eleves=eleves)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return "An error occurred"

# ➕ Ajouter une note
@app.route('/ajouter_note_prof', methods=['POST'])
def ajouter_note_prof():
    if 'username' not in session or session['role'] != 'prof':
        return redirect(url_for('login_form'))

    identifiant = request.form['identifiant']
    note = request.form['note']
    trimestre = request.form['trimestre']
    matiere = request.form['matiere']

    try:
        conn = sqlite3.connect("ecole.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notes (Identifiant, note, Trimestre, Matiere) VALUES (?, ?, ?, ?)", 
                       (identifiant, note, trimestre, matiere))
        conn.commit()
        conn.close()
        return redirect(url_for('tableau_prof'))
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return "An error occurred"

# ✏️ Modifier une note
@app.route('/modifier_note/<identifiant>/<trimestre>', methods=['POST'])
def modifier_note(identifiant, trimestre):
    if 'username' not in session or session['role'] != 'prof':
        return redirect(url_for('login_form'))
    
    nouvelle_note = request.form['note']
    
    try:
        conn = sqlite3.connect("ecole.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE notes SET note = ? WHERE Identifiant = ? AND Trimestre = ?", 
                       (nouvelle_note, identifiant, trimestre))
        conn.commit()
        conn.close()
        return redirect(url_for('tableau_prof'))
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return "An error occurred"

# ❌ Supprimer une note
@app.route('/supprimer_note/<identifiant>/<trimestre>')
def supprimer_note(identifiant, trimestre):
    if 'username' not in session or session['role'] != 'prof':
        return redirect(url_for('login_form'))
    
    try:
        conn = sqlite3.connect("ecole.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM notes WHERE Identifiant = ? AND Trimestre = ?", (identifiant, trimestre))
        conn.commit()
        conn.close()
        return redirect(url_for('tableau_prof'))
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return "An error occurred"

# 📖 Voir les notes d'un élève (SEULEMENT SES NOTES)
@app.route('/mes_notes')
def mes_notes():
    if 'username' not in session or session['role'] != 'eleve':
        return redirect(url_for('login_form'))
    
    identifiant = session['username']
    
    try:
        conn = sqlite3.connect("ecole.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT n.Matiere, n.Trimestre, n.note, 
                   (SELECT AVG(note) FROM notes WHERE Matiere = n.Matiere AND Trimestre = n.Trimestre) 
            FROM notes n 
            WHERE n.Identifiant = ?
            ORDER BY n.Trimestre, n.Matiere
        """, (identifiant,))
        raw_notes = cursor.fetchall()
        conn.close()

        notes_dict = {}
        for matiere, trimestre, note, moyenne_classe in raw_notes:
            key = (matiere, trimestre, round(moyenne_classe, 1))
            if key not in notes_dict:
                notes_dict[key] = []
            notes_dict[key].append(note)

        grouped_notes = [(m, t, mc, notes) for (m, t, mc), notes in notes_dict.items()]

        return render_template('Note.html', grouped_notes=grouped_notes)

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return "An error occurred"

# 🔑 Formulaire de connexion
@app.route('/')
def login_form():
    return render_template('connection.html')

# 🔑 Traitement du login
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    role = check_login(username, password)
    
    if role:
        session['username'] = username
        session['role'] = role
        return redirect(url_for('nav') if role == "eleve" else url_for('tableau_prof'))
    else:
        return render_template('connection.html', error="Nom d'utilisateur ou mot de passe incorrect.")

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('login_form'))

# 📌 Navigation générale
@app.route('/nav')
def nav():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login_form'))

# 🕒 Emploi du temps
@app.route('/timetable')
def timetable():
    return render_template('emploidutemps.html')

# 📊 Notes
@app.route('/Note')
def Note():
    return redirect(url_for('mes_notes'))

# 📊 Classe
@app.route('/classe')
def classe():
    return render_template('classe.html')

@app.route('/tab_prof')
def tab_prof():
    return render_template('TableauProf.html')

@app.route('/time_prof')
def time_prof():
    return render_template('emploisdutempsprof.html')

@app.route('/aide')
def aide():
    return render_template('aide.html')

@app.route('/parametres')
def parametres():
    return render_template('parametres.html')

@app.route('/aide_prof')
def aide_prof():
    return render_template('aide_prof.html')

@app.route('/parametres_prof')
def parametres_prof():
    return render_template('parametres_prof.html')

if __name__ == '__main__':
    app.run(debug=True)
