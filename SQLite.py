import sqlite3

def create_database():
    conn = sqlite3.connect("ecole.db")
    cursor = conn.cursor()

    cursor.executescript("""
        -- Création de la table des utilisateurs
        CREATE TABLE IF NOT EXISTS users (
            Identifiant TEXT PRIMARY KEY,
            Nom TEXT NOT NULL,
            Prenom TEXT NOT NULL,
            Mot_de_passe TEXT NOT NULL,
            Role TEXT CHECK(Role IN ('admin', 'prof', 'eleve')) NOT NULL
        );

        -- Création de la table des notes
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Identifiant TEXT NOT NULL,
            Matiere TEXT NOT NULL,
            Trimestre INTEGER NOT NULL,
            note REAL CHECK(note >= 0 AND note <= 20) NOT NULL,
            FOREIGN KEY (Identifiant) REFERENCES users (Identifiant)
        );

        -- Création de la table des élèves (SQLAlchemy)
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            status TEXT DEFAULT 'Présent'
        );

        -- Création de la table "eleves"
        CREATE TABLE IF NOT EXISTS eleves (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            statut TEXT DEFAULT 'Présent'
        );
    """)

    conn.commit()
    conn.close()
    print("Base de données créée avec succès !")

def populate_database():
    conn = sqlite3.connect("ecole.db")
    cursor = conn.cursor()

    # 📌 Ajout d'utilisateurs (Admins, Profs, Élèves)
    cursor.executemany("""
        INSERT OR IGNORE INTO users (Identifiant, Nom, Prenom, Mot_de_passe, Role) VALUES (?, ?, ?, ?, ?)
    """, [
        ('admin', 'Dupont', 'Jean', '1234', 'admin'),
        ('Antony', 'Martin', 'Antony', 'test1', 'eleve'),
        ('Phillipe', 'Durand', 'Phillipe', 'test2', 'eleve'),
        ('Orane', 'Lemoine', 'Orane', 'test3', 'prof'),
        ('admin2', 'Bernard', 'Luc', 'adminpass', 'admin'),
        ('eleve1', 'Petit', 'Julie', 'elevepass1', 'eleve'),
        ('eleve2', 'Robert', 'Paul', 'elevepass2', 'eleve'),
        ('prof1', 'Garcia', 'Laura', 'profpass1', 'prof'),
        ('prof2', 'Simon', 'Nicolas', 'profpass2', 'prof')
    ])

    # 📌 Ajout des élèves dans la table "eleves"
    cursor.executemany("""
        INSERT OR IGNORE INTO eleves (nom, email, statut) VALUES (?, ?, ?)
    """, [
        ('Martin', 'martin@example.com', 'Présent'),
        ('Durand', 'durand@example.com', 'Absent'),
        ('Lemoine', 'lemoine@example.com', 'Présent'),
        ('Garcia', 'garcia@example.com', 'Absent'),
        ('Bernard', 'bernard@example.com', 'Présent'),
        ('Petit', 'petit@example.com', 'Absent'),
        ('Robert', 'robert@example.com', 'Présent'),
        ('Simon', 'simon@example.com', 'Présent')
    ])

    # 📌 Ajout des élèves dans la table "student" (SQLAlchemy)
    cursor.executemany("""
        INSERT OR IGNORE INTO student (name, email, status) VALUES (?, ?, ?)
    """, [
        ('Alice', 'alice@example.com', 'Présent'),
        ('Bob', 'bob@example.com', 'Absent'),
        ('Charlie', 'charlie@example.com', 'Présent'),
        ('David', 'david@example.com', 'Présent'),
        ('Emma', 'emma@example.com', 'Absent'),
        ('Fabrice', 'fabrice@example.com', 'Présent'),
        ('Giselle', 'giselle@example.com', 'Absent')
    ])

    # 📌 Ajout des notes
    cursor.executemany("""
        INSERT OR IGNORE INTO notes (Identifiant, Matiere, Trimestre, note) VALUES (?, ?, ?, ?)
    """, [
        ('Antony', 'Maths', 1, 15.5),
        ('Antony', 'Maths', 2, 13.0),
        ('Antony', 'Français', 1, 12.0),
        ('Phillipe', 'Maths', 1, 17.0),
        ('Phillipe', 'Français', 1, 14.5),
        ('Orane', 'Histoire', 2, 18.0),
        ('eleve1', 'Maths', 1, 16.0),
        ('eleve2', 'Maths', 1, 14.0),
        ('eleve1', 'Physique', 2, 10.5),
        ('eleve2', 'SVT', 3, 19.0),
        ('eleve2', 'Anglais', 2, 11.5),
        ('eleve1', 'Sport', 3, 20.0)
    ])

    conn.commit()
    conn.close()
    print("✅ Base de données remplie avec succès !")

if __name__ == "__main__":
    create_database()
    populate_database()
