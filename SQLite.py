import sqlite3

def create_database():
    try:
        conn = sqlite3.connect("ecole.db")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            Identifiant TEXT PRIMARY KEY NOT NULL,
            Mot_de_passe TEXT NOT NULL
        );
        """)

        users = [
            ('admin', '1234'),
            ('Antony', 'test1'),
            ('Phillipe', 'test2'),
            ('Orane', 'test3')
        ]

        cursor.executemany("INSERT OR IGNORE INTO users (Identifiant, Mot_de_passe) VALUES (?, ?)", users)

        conn.commit()
        conn.close()
        print("Base de données et table créées avec succès.")

    except sqlite3.DatabaseError as e:
        print(f"Erreur de base de données : {e}")

if __name__ == "__main__":
    create_database()
