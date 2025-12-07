[[__TOC__]]

# Exercices pour la formation Python : TP5 

Rappel pour s'assurer d'avoir toutes les librairies nécessaires pour le TP:
```sh
pip install -r requirements.txt
```

# PyArrow

PyArrow est une bibliothèque qui fournit des structures de données colonnaires en mémoire pour traiter efficacement de gros volumes de données. Elle est particulièrement utile pour l'analyse de données, l'échange entre systèmes et l'optimisation des performances.

## Introduction à PyArrow

PyArrow offre :
- Des structures de données colonnaires optimisées
- Une intégration native avec Pandas, NumPy et Parquet
- Des opérations vectorisées ultra-rapides
- Une gestion efficace de la mémoire
- Un support pour les données manquantes optimisé


## Fonction utile pour le TP :

```python
import pyarrow as pa
import pyarrow.compute as pc
import pytest
import numpy as np
import pandas as pd
import pyarrow.parquet as pq
import pyarrow.csv as pcsv


# Fonctions de création
pa.array()              # Créer un Array PyArrow
pa.table()              # Créer une Table PyArrow
pa.schema()             # Définir un schéma
pa.field()              # Définir un champ
pq.ParquetDataset(partitioned_path) # Créer un dataset a partir d'un chemin ayant des fichiers parquet partionné

# Fonctions de lecture/écriture
pq.read_table()         # Lire un fichier Parquet
pq.write_table()        # Écrire un fichier Parquet
csv.read_csv()          # Lire un fichier CSV
dataset.read()          # Lire le dataset vers le format table de pyarrow

# Fonctions compute (opérations vectorisées)
pc.sum()                # Somme
pc.mean()               # Moyenne
pc.min(), pc.max()      # Min/Max
pc.count()              # Compter
pc.filter()             # Filtrer
pc.sort_indices()       # Trier
pc.group_by()           # Grouper
pc.join()               # Jointure

# Fonctions utiles sur Arrays/Tables
.as_py()                # Répresentation python d'un scalar. ex: <pyarrow.Int64Scalar: 1> = 1
.to_numpy()             # Convertir vers NumPy
.to_pandas()            # Convertir vers Pandas
.cast()                 # Changer de type
.slice()                # Découper
.take()                 # Sélectionner par indices
.null_count             # Compter les valeurs nulles
.length                 # Taille
.type                   # Type de données
.schema                 # Schéma (pour Tables)
.column_names           # Noms des colonnes (pour Tables)
.select()               # Sélectionner des colonnes
```

Voici les fixtures PyArrow disponibles pour vos tests :

```python

@pytest.fixture
def array_simple() -> pa.Array:
    """ Array PyArrow simple pour les tests """
    return pa.array([1, 2, 3, 4, 5])

@pytest.fixture
def table_simple() -> pa.Table:
    """ Table PyArrow simple pour les tests """
    data = {
        'nom': pa.array(['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']),
        'age': pa.array([25, 30, 35, 28, 22]),
        'salaire': pa.array([50000, 60000, 75000, 55000, 48000]),
        'departement': pa.array(['IT', 'RH', 'IT', 'Marketing', 'RH'])
    }
    return pa.table(data)
```

### Exercice 1 : Création et manipulation de base d'Arrays et Tables

1. **Création d'Arrays PyArrow** :
   - Créez un Array PyArrow à partir d'une liste Python
   - Créez un Array à partir d'un array NumPy
   - Créez un Array avec des valeurs manquantes (null)
   - Explorez les différents types de données PyArrow

2. **Propriétés des Arrays** :
   - Affichez la longueur, le type et les statistiques d'un Array
   - Vérifiez la présence de valeurs nulles
   - Calculez des statistiques de base (min, max, sum)

3. **Création de Tables** :
   - Créez une Table PyArrow à partir de dictionnaires
   - Convertissez un DataFrame Pandas en Table PyArrow
   - Explorez les métadonnées et le schéma d'une Table

### Exercice 2 : Conversion et interopérabilité

1. **Conversions bidirectionnelles** :
   - Convertissez entre PyArrow Arrays et NumPy arrays
   - Convertissez entre PyArrow Tables et Pandas DataFrames
   - Gérez les types de données lors des conversions

### Exercice 3 : Opérations sur les données

1. **Filtrage et sélection** :
   - Filtrez des Tables avec des conditions
   - Sélectionnez des colonnes spécifiques

2. **Agrégations et groupements** :
   - Calculez des agrégations sur les colonnes
   - Groupez des données par une ou plusieurs colonnes

3. **Jointures et concaténation** :
   - Joignez plusieurs Tables
   - Concaténez des Tables verticalement et horizontalement
   - Gérez les jointures avec des clés multiples (optionnel)

### Exercice 4 : Lecture et écriture de fichiers

1. **Format Parquet** :
   - Écrivez une Table PyArrow en format Parquet
   - Lisez des fichiers Parquet avec différentes options

2. **Format CSV ** :
   - Lisez des fichiers CSV avec PyArrow

3. **Datasets partitionnés** :
   - Créez des datasets partitionnés
   - Lisez des datasets multi-fichiers


### Conseils pour la résolution

- Utilisez `pa.array()` et `pa.table()` pour créer des structures PyArrow
- Exploitez le zero-copy quand c'est possible avec `.to_numpy(zero_copy_only=False)`
- Mesurez toujours les performances avec `%timeit` en Jupyter
- Utilisez `pa.compute` pour les opérations vectorisées
- Privilégiez les formats colonnaires pour les analyses
- Testez avec de vrais gros datasets pour voir les bénéfices

### Ressources utiles

- [Documentation officielle PyArrow](https://arrow.apache.org/docs/python/)
- [PyArrow Cookbook](https://arrow.apache.org/cookbook/py/)
- [Guide Pandas PyArrow](https://pandas.pydata.org/docs/user_guide/pyarrow.html)
- [Format Parquet](https://parquet.apache.org/docs/)
- [Arrow Compute Functions](https://arrow.apache.org/docs/python/api/compute.html)