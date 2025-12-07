[[__TOC__]]

# Exercices pour la formation Python : TP5 

Rappel pour s'assurer d'avoir toutes les librairies nécessaires pour le TP:
```sh
pip install -r requirements.txt
```

# PyODBC

PyODBC est une bibliothèque Python qui permet de se connecter et d'interagir avec des bases de données via ODBC (Open Database Connectivity)

## Introduction à PyODBC

PyODBC offre :
- Une interface Python pour les bases de données ODBC
- Une compatibilité avec SQL Server, PostgreSQL, MySQL, Oracle, etc.
- Une gestion robuste des transactions
- Un support des procédures stockées et des requêtes paramétrées
- Une intégration avec l'écosystème Python de data science

## Context

Pour s'assurer de la faisabilité du TP nous allons utiliser pysqlite3 au lieu de pyodbc qui offre des fonctionnalité similaire a pyodbc ormis qu'elle est dédié au base de données sqlite3 in memory et fichier.  

## Fonctions utiles pour le TP :

```python
import pyodbc
import pandas as pd
import numpy as np

# Fonctions utiles pour la résolution des exercices :
pyodbc.connect(connection_string)  # Connexion à la base de données
cursor = conn.cursor()            # Création d'un curseur
cursor.execute(sql_query)         # Exécution d'une requête
cursor.fetchall()                 # Récupération de tous les résultats
cursor.fetchone()                 # Récupération d'un résultat
cursor.fetchmany(size)            # Récupération de n résultats
pd.read_sql(query, connection)    # Lecture SQL vers DataFrame
df.to_sql(name, con, if_exists)   # Écriture DataFrame vers SQL
cursor.commit()                   # Validation des transactions
cursor.rollback()                 # Annulation des transactions
pyodbc.drivers()                  # Liste des drivers disponibles

# Gestion des paramètres et sécurité :
cursor.execute("SELECT * FROM table WHERE id = ?", (value,))
cursor.executemany(sql, params_list)  # Exécution en lot


# Fonctions utiles pour faire vos assertions :
assert len(results) > 0
assert isinstance(df, pd.DataFrame)
assert not df.empty
```

Voici les fixtures PyODBC disponibles pour vos tests :

```python

@pytest.fixture
def sqlite_connection():
    """
    Connexion SQLite en mémoire pour les tests
    """
    return sqlite3.connect(':memory:')    

@pytest.fixture
def sample_data():
    """Données d'exemple pour les tests"""
    return [
        (1, 'Alice', 25, 50000, 'IT'),
        (2, 'Bob', 30, 60000, 'RH'),
        (3, 'Charlie', 35, 75000, 'IT'),
        (4, 'Diana', 28, 55000, 'Marketing'),
        (5, 'Eve', 22, 48000, 'RH')
    ]
```

### Exercice 1 : Connexion et configuration de base

1. **Établissement de connexion** :
   - Créez une connexion à une base de données SQLite
   - Gérez les erreurs de connexion

2. **Configuration et métadonnées** :
   - Explorez les tables et colonnes disponibles

3. **Gestion des ressources** :
   - Implémentez une connexion avec context manager
   - Gérez la fermeture propre des connexions

### Exercice 2 : Requêtes SQL de base et manipulation de données

1. **Opérations CRUD** :
   - Créez des tables avec CREATE TABLE
   - Insérez des données avec INSERT
   - Mettez à jour des enregistrements avec UPDATE
   - Supprimez des données avec DELETE

2. **Requêtes de sélection** :
   - Exécutez des SELECT avec filtres WHERE
   - Utilisez ORDER BY et LIMIT pour l'organisation
   - Implémentez des jointures entre tables
   - Créez des requêtes d'agrégation (GROUP BY, HAVING)

3. **Récupération de résultats** :
   - Utilisez fetchall(), fetchone(), fetchmany()
   - Parcourez les résultats avec des itérateurs
   - Convertissez les résultats en dataframe

### Exercice 3 : Sécurité et requêtes paramétrées

1. **Prévention des injections SQL** :
   - Utilisez des paramètres liés (?) pour les valeurs
   - Validez et échappez les entrées utilisateur

2. **Requêtes complexes paramétrées** :
   - Créez des requêtes avec paramètres multiples
   - Utilisez des paramètres nommés quand possible

3. **Exécution en lot** :
   - Utilisez executemany() pour les insertions multiples

### Exercice 4 : Intégration avec Pandas et analyse de données

1. **Pandas et SQL** :
   - Chargez des DataFrames depuis SQL avec read_sql()
   - Écrivez des DataFrames vers SQL avec to_sql()
   - Gérez les types de données lors des conversions
   - Implémentez des jointures SQL/DataFrame

### Exercice 5 : Gestion des transactions et erreurs

1. **Transactions** :
    - Implémentez des transactions avec commit/rollback
    - Optimisez les performances transactionnelles
    - Implémentez des retry automatiques
    - Créez des mécanismes de fallback

### Conseils pour la résolution

- Utilisez toujours des paramètres liés pour éviter les injections SQL
- Loggez les requêtes pour le debugging
- Gérez les erreurs de réseau et de timeout avec des retry
- Utilisez des transactions pour les opérations critiques

### Ressources utiles

- [Documentation officielle PyODBC](https://github.com/mkleehammer/pyodbc/wiki)
- [PyODBC Examples](https://github.com/mkleehammer/pyodbc/wiki/Examples)
- [SQL Server et PyODBC](https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/python-sql-driver-pyodbc)
- [Postgresql et PyODBC](https://odbc.postgresql.org/)
- [ODBC Data Sources](https://docs.microsoft.com/en-us/sql/odbc/reference/data-sources)
- [Performance Tuning](https://github.com/mkleehammer/pyodbc/wiki/Performance)
