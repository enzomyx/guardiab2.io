import sqlite3

def create_database():
    try:
        conn = sqlite3.connect("ecole.db")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            Identifiant TEXT PRIMARY KEY NOT NULL,
            Nom TEXT NOT NULL,
            Prenom TEXT NOT NULL,
            Mot_de_passe TEXT NOT NULL,
            Role TEXT NOT NULL CHECK (Role IN ('eleve', 'prof', 'admin')),
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id_note INTEGER PRIMARY KEY AUTOINCREMENT,
            Identifiant TEXT NOT NULL,
            note INTEGER NOT NULL,
            Matiere TEXT NOT NULL,
            Trimestre TEXT NOT NULL,
            FOREIGN KEY (Identifiant) REFERENCES users (Identifiant)
        );
        """)

        cursor.executemany("""
        INSERT OR IGNORE INTO users (Identifiant, Nom, Prenom, Mot_de_passe, Role) VALUES (?, ?, ?, ?, ?)
        """, [
            ('admin', 'Dupont', 'Jean', '1234', 'admin'),
            ('Antony', 'Martin', 'Antony', 'test1', 'eleve'),
            ('Phillipe', 'Durand', 'Phillipe', 'test2', 'eleve'),
            ('Orane', 'Lemoine', 'Orane', 'test3', 'prof')
        ])

        cursor.executemany("""
        INSERT OR IGNORE INTO notes (Identifiant, note, Matiere, Trimestre) VALUES (?, ?, ?, ?)
        """, [
            ('Antony', 15, 'Mathématiques', 'Trimestre 1'),
            ('Antony', 12, 'Français', 'Trimestre 2'),
            ('Antony', 8, 'Mathématiques', 'Trimestre 2'),
            ('Phillipe', 12, 'Français', 'Trimestre 2')
        ])

        conn.commit()
        conn.close()
        print("Base de données mise à jour avec succès.")

    except sqlite3.DatabaseError as e:
        print(f"Erreur de base de données : {e}")

if __name__ == "__main__":
    create_database()
