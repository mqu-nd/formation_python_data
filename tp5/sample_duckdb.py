# %%
import duckdb
import pandas as pd

clients = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'nom': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'age': [30, 25, 35, 28, 42, 37],
    'ville': ['Paris', 'Lyon', 'Paris', 'Nantes', 'Lyon', 'Nantes']
})
clients.to_csv('clients.csv', index=False)


# 1) Créer une connexion en mémoire (aucun serveur requis)
con = duckdb.connect()

# 2) Lire un fichier CSV et exécuter une requête SQL
result = con.execute("""
    SELECT ville, COUNT(*) AS nb_clients
    FROM read_csv_auto('clients.csv')
    GROUP BY ville
    ORDER BY nb_clients DESC
""").fetchdf()

# 3) Afficher le résultat sous forme de DataFrame pandas
print(result)

# %%
