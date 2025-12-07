# %%
import sqlite3

# 1. Créer ou se connecter à une base SQLite (fichier ou mémoire)
conn = sqlite3.connect("demo.db")  # crée demo.db si n'existe pas

# 2. Créer un curseur
cursor = conn.cursor()

# 3. Créer une table (si elle n'existe pas)
cursor.execute("""
CREATE TABLE IF NOT EXISTS Clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    ville TEXT
)
""")

# 4. Insérer des données
cursor.execute("INSERT INTO Clients (nom, ville) VALUES (?, ?)", ("Alice", "Paris"))
cursor.execute("INSERT INTO Clients (nom, ville) VALUES (?, ?)", ("Bob", "Lyon"))

# Valider la transaction
conn.commit()

# 5. Lire les données
cursor.execute("SELECT id, nom, ville FROM Clients")
for row in cursor.fetchall():
    print(f"ID: {row[0]}, Nom: {row[1]}, Ville: {row[2]}")

# 6. Fermer la connexion
cursor.close()
conn.close()

# %%
