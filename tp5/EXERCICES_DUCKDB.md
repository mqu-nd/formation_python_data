[[__TOC__]]

# Exercices pour la formation Python : TP5 

Rappel pour s'assurer d'avoir toutes les librairies nécessaires pour le TP:
```sh
pip install -r requirements.txt
```

# DuckDB

DuckDB est une base de données analytique en mémoire (OLAP) conçue pour être intégrée dans des applications. Elle excelle dans l'analyse de données avec des performances exceptionnelles sur des requêtes analytiques complexes et s'intègre parfaitement avec l'écosystème Python de data science.

## Introduction à DuckDB

DuckDB offre :
- Une base de données SQL complète sans serveur
- Des performances exceptionnelles sur les requêtes analytiques
- Une intégration native avec Pandas, NumPy et PyArrow
- Un support natif pour les formats Parquet, CSV, JSON
- Des fonctions vectorisées optimisées
- Une syntaxe SQL standard avec des extensions analytiques

### Premier pas avec duckdb via dbeaver :

Nécessite d'avoir dbeaver et le driver installé pour cette partie.
https://dbeaver.io/download/
https://duckdb.org/docs/stable/guides/sql_editors/dbeaver

1. **Connexion et création de tables** :
   - Créez une connexion DuckDB en mémoire via Dbeaver
   - Lisez un fichier csv
   - Créez une table à partir de ce fichier

### Exercice 1 : Création et manipulation de base avec DuckDB

1. **Connexion et création de tables** :
   - Créez une connexion DuckDB en mémoire
   - Créez des tables à partir de données Python
   - Importez des DataFrames Pandas directement
   - Explorez les types de données DuckDB

2. **Requêtes SQL de base** :
   - Exécutez des requêtes SELECT simples
   - Utilisez des clauses WHERE, ORDER BY, LIMIT
   - Calculez des agrégations (COUNT, SUM, AVG, MIN, MAX)
   - Récupérez les résultats en DataFrame

3. **Insertion et mise à jour** :
   - Insérez des données avec INSERT
   - Mettez à jour des enregistrements avec UPDATE
   - Supprimez des données avec DELETE
   - Créer une transaction

### Exercice 2 : Intégration avec l'écosystème Python

# 1. **Pandas et DuckDB** :
    - Enregistrez des DataFrames comme tables temporaires
    - Exécutez du SQL directement sur des DataFrames
    - Convertissez des résultats SQL en DataFrames
    
# 2. **PyArrow et formats colonnaires** :
    - Travaillez avec des Tables PyArrow
    - Lisez des fichiers Parquet directement

# 3. **NumPy et calculs vectorisés** :
    - Intégrez des arrays NumPy dans des requêtes
    - Utilisez des fonctions mathématiques comme écart-type

### Exercice 3 : Requêtes analytiques avancées

1. **Fonctions de fenêtre (Window Functions)** :
   - Calculez des rangs et percentiles
   - Implémentez des moyennes mobiles
   - Utilisez LAG/LEAD pour des comparaisons temporelles
   - Créez des partitions pour des analyses groupées

2. **Requêtes hiérarchiques et récursives** :
   - Utilisez des CTE (Common Table Expressions)
   - Implémentez des requêtes récursives
   - Analysez des structures d'arbre
   - Calculez des chemins et des niveaux

3. **Données semi-structurées** :
   - Parsez des données JSON complexes
   - Extrayez des éléments de structures imbriquées
   - Convertissez entre formats structurés


### Conseils pour la résolution

- Utilisez `duckdb.connect()` pour créer des connexions
- Utilisez `EXPLAIN` pour analyser les plans de requête
- Privilégiez les requêtes SQL pour les opérations lourdes
- Combinez SQL et Python pour des workflows hybrides

### Ressources utiles

- [Documentation officielle DuckDB](https://duckdb.org/docs/)
- [DuckDB Python API](https://duckdb.org/docs/api/python/overview.html)
- [SQL Reference DuckDB](https://duckdb.org/docs/sql/introduction)
- [Extensions DuckDB](https://duckdb.org/docs/extensions/overview)
- [Performance Guide](https://duckdb.org/docs/guides/performance/how_to_tune_workloads.html)
