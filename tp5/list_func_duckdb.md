# Connexion & exécution (API Python)

con = duckdb.connect(database=None) # Créer une connexion (en mémoire ou fichier .duckdb).
con.execute(sql, parameters=None) # Exécuter une requête SQL.
con.sql(sql) # Alias pratique de execute qui retourne un Relation (chaînable).
con.close() # Fermer la connexion.

Exemple :
```python
con = duckdb.connect()                      # ou duckdb.connect("warehouse.duckdb")
con.execute("CREATE TABLE t(a INT, b TEXT)")
con.execute("INSERT INTO t VALUES (1, 'x'), (2, 'y')")
con.close()
```

# Récupération des résultats / Interopérabilité

fetchdf() # Retourne un DataFrame pandas.
fetch_arrow_table() # Retourne une PyArrow Table.
fetchnumpy() # Retourne un dict de tableaux NumPy.
fetchall() / fetchone() # Retourne des tuples Python.

Exemple :
```python
df = con.execute("SELECT * FROM t").fetchdf()
tbl = con.execute("SELECT * FROM t").fetch_arrow_table()
np_data = con.execute("SELECT a FROM t").fetchnumpy()
rows = con.execute("SELECT b FROM t").fetchall()
```

# Lecture directe de fichiers (sans ETL)

Parquet : SELECT * FROM 'data.parquet'
CSV (auto) : SELECT * FROM read_csv_auto('data.csv')
JSON (avec extension) : SELECT * FROM read_json_auto('data.json')

Exemple :
```python
df_parquet = con.execute("SELECT * FROM 'clients.parquet'").fetchdf()
df_csv = con.execute("SELECT * FROM read_csv_auto('clients.csv')").fetchdf()
```

# Export de données
COPY ( <query> ) TO 'file.parquet' (FORMAT PARQUET) # Export Parquet.
COPY ( <query> ) TO 'file.csv' (HEADER, DELIMITER ',') # Export CSV.
CREATE TABLE ... AS SELECT ... # Matérialiser le résultat en table DuckDB.

Exemple :
```python
con.execute("""
  COPY (
    SELECT ville, COUNT(*) AS nb_clients
    FROM 'clients.parquet'
    GROUP BY ville
  ) TO 'stats.parquet' (FORMAT PARQUET)
""")
```

# Interopérabilité mémoire (pandas / PyArrow / Polars)

register(name, object) # Enregistrer un objet en mémoire comme table (pandas/Arrow).
unregister(name) # Supprimer l’enregistrement.

Exemple :
```python
import pandas as pd
df = pd.DataFrame({"a":[1,2], "b":["x","y"]})
con.register("df_view", df)
out = con.execute("SELECT * FROM df_view WHERE a=2").fetchdf()
con.unregister("df_view")
```

# Gestion de schéma et de données (DDL/DML)

CREATE TABLE, CREATE VIEW # Créer structure ou vue logique.
INSERT, UPDATE, DELETE # Modifier des données.
ATTACH 'file.duckdb' AS alias / DETACH alias # Gérer plusieurs bases.

Exemple :
```python
con.execute("CREATE TABLE clients AS SELECT * FROM 'clients.parquet'")
con.execute("UPDATE clients SET age = age + 1 WHERE ville='Paris'")
```

# SQL analytique — fonctions fréquentes

Agrégations / Group By : COUNT, SUM, AVG, MIN, MAX.
Window functions : ROW_NUMBER(), RANK(), LEAD/LAG, PARTITION BY.
Jointures : JOIN, LEFT JOIN, RIGHT JOIN.
Filtres & projections : WHERE, SELECT, ORDER BY, LIMIT.

Exemple :
```sql
SELECT ville, COUNT(*) AS nb
FROM clients
GROUP BY ville
ORDER BY nb DESC;
```

# Extensions & accès distant

INSTALL <extension>; LOAD <extension>; # Activer fonctionnalités (ex: httpfs, json).
Accès S3/HTTP avec httpfs (et variables de conf).
read_json_auto() pour JSON (après INSTALL json).

Exemple :
```sql
INSTALL httpfs; LOAD httpfs;
-- Exemple: lire un Parquet sur S3 (credentials requis)
SELECT * FROM 's3://mon-bucket/clients.parquet';
```

# Performance, diagnostics, contrôle

PRAGMA threads=8 # Régler le parallélisme.
PRAGMA memory_limit='2GB' # Limiter la mémoire.
EXPLAIN / EXPLAIN ANALYZE # Voir le plan et le profil d’exécution.
ANALYZE table # Statistiques pour optimiser le planneur.
PRAGMA enable_object_cache # Activer le cache d’objets.

Exemple :
```sql
EXPLAIN ANALYZE
SELECT ville, COUNT(*) FROM clients GROUP BY ville;
```

# Utilitaires SQL pratiques
SHOW TABLES; # Lister les tables.
DESCRIBE table; # Voir les colonnes et types.
PARQUET_SCAN('file.parquet') # Scan performant (équivalent à 'file.parquet').
read_csv_auto('file.csv') # Lecture CSV avec détection automatique.