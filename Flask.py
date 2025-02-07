from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import secrets

app = Flask(__name__)

app.secret_key = secrets.token_hex(32)


def check_login(username, password):
    """ Vérifie si l'utilisateur existe dans la base de données. """
    conn = sqlite3.connect('ecole.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE Identifiant = ? AND Mot_de_passe = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    
    return user is not None


@app.route('/')
def login_form():
    """ Affiche la page de connexion """
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    """ Gère la connexion de l'utilisateur """
    username = request.form.get('username')
    password = request.form.get('password')

    print(f"DEBUG: Username: {username}, Password: {password}")
    if not username or not password:
        return render_template('login.html', error="Veuillez remplir tous les champs.")

    if check_login(username, password):
        session['username'] = username
        return redirect(url_for('nav'))
    else:
        return render_template('login.html', error="Nom d'utilisateur ou mot de passe incorrect.")

@app.route('/nav')
def nav():
    """ Affiche la page Nav si l'utilisateur est connecté """
    if 'username' in session:
        return render_template('Nav.html', username=session['username'])
    return redirect(url_for('login_form'))

@app.route('/NAV')
def NAV():
    return render_template('Nav.html')

@app.route('/timetable')
def timetable():
    return render_template('Timetable.html')

@app.route('/Note')
def Note():
    return render_template('Note.html')


@app.route('/logout')
def logout():
    """ Déconnexion de l'utilisateur """
    session.pop('username', None)
    return redirect(url_for('login_form'))


if __name__ == '__main__':
    app.run(debug=True)
