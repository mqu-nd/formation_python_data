import pyodbc

# Connexion
# exemple de chaîne de connexion
conn_str = ("DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=ma_base_de_donnees;"
    "UID=mon_utilisateur;"
    "PWD=mon_mot_de_passe;")
conn = pyodbc.connect(conn_str) # Établit la connexion à la base.
cursor = conn.cursor() # Crée un curseur pour exécuter des requêtes.
conn.commit() # Valide les modifications.
conn.rollback() # Annule les modifications.
conn.close() # Ferme la connexion.


# Exécution de requêtes
cursor.execute(sql, params) # Exécute une requête SQL (avec paramètres ?).
cursor.executemany(sql, list_of_params) # Exécute une requête en lot.
cursor.fast_executemany = True # Active l’optimisation pour les inserts en masse.


# Lecture des résultats

cursor.fetchone() # Récupère une ligne.
cursor.fetchmany(n) # Récupère n lignes.
cursor.fetchall() # Récupère toutes les lignes.
for row in cursor: # Parcourt les résultats en streaming.

# Infos sur le résultat

cursor.description # Structure des colonnes (nom, type, etc.).
cursor.rowcount # Nombre de lignes affectées par la dernière requête.

# Autres pratiques utiles
with conn.cursor() as cur: # Curseur avec fermeture automatique.
conn.setencoding('utf-8') # Définit l’encodage.
conn.timeout = 30 # Timeout de la connexion.

# Placeholders & Sécurité
# Utiliser ? pour les paramètres :
cursor.execute("SELECT * FROM Clients WHERE ville = ?", ("Paris",))