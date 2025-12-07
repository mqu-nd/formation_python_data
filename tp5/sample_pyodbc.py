
import pyodbc

# 1. Définir la chaîne de connexion (adapter selon votre SGBD)
conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=DemoDB;"
    "UID=demo_user;"
    "PWD=demo_password;"
    "TrustServerCertificate=yes;"
)

# 2. Établir la connexion
conn = pyodbc.connect(conn_str)

# 3. Créer un curseur
cursor = conn.cursor()

# 4. Exécuter une requête SQL
cursor.execute("SELECT TOP 5 id, nom FROM Clients")

# 5. Parcourir les résultats
for row in cursor.fetchall():
    print(f"ID: {row.id}, Nom: {row.nom}")

# 6. Fermer la connexion
cursor.close()
conn.close()
