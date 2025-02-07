import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur la page d'accueil du serveur Flask !"

@app.route('/create_db')
def create_db():
    try:
        conn = sqlite3.connect('école1.db')
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,  
            Prénom VARCHAR(100) NOT NULL,
            Nom VARCHAR(100) NOT NULL,
            Matière VARCHAR(100) NOT NULL,
            Classe VARCHAR(100) NOT NULL,
            Identifiant TEXT NOT NULL,
            Mot_de_passe TEXT NOT NULL
        );
        ''')

        cursor.execute("""
        INSERT OR IGNORE INTO users (Prénom, Nom, Matière, Classe, Identifiant, Mot_de_passe) 
        VALUES 
            ('Antony', 'Test', '', 'GSC', 'Antony', 'test1'), 
            ('Phillippe', 'Kaadi', 'Français', '', 'Phillipe', 'test2'), 
            ('Orane', 'Mainville', '', 'GSC', 'Orane', 'test3')
        """)

        conn.commit()
        conn.close()

        return "Base de données et table créées avec succès."
    except sqlite3.DatabaseError as e:
        return f"Erreur de base de données : {e}"

if __name__ == '__main__':
    app.run(debug=True)
