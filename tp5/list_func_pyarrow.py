import pyarrow

# 1. Lecture et écriture de fichiers

pyarrow.parquet.read_table(path) # Lire un fichier Parquet en tant que Table Arrow.
pyarrow.parquet.write_table(table, path) # Écrire une Table Arrow en Parquet.
pyarrow.feather.read_table(path) # Lire un fichier Feather.
pyarrow.feather.write_feather(table, path) # Écrire en Feather.


# 2. Conversion entre formats

table.to_pandas() # Convertir une Table Arrow en DataFrame pandas.
pyarrow.Table.from_pandas(df) # Convertir un DataFrame pandas en Table Arrow.
pyarrow.array() # Créer un tableau Arrow à partir d’une liste Python.


# 3. Création et manipulation de tables

pyarrow.Table.from_arrays(arrays, names) # Créer une Table à partir de plusieurs colonnes.
table.column(index) # Accéder à une colonne par index.
table.select(columns) # Sélectionner des colonnes spécifiques.
table.slice(offset, length) # Découper une Table.


# 4. Gestion des schémas

table.schema # Obtenir le schéma (types et noms des colonnes).
pyarrow.schema(fields) # Créer un schéma personnalisé.


# 5. Compression et options avancées

pyarrow.parquet.write_table(table, path, compression='snappy') # Écrire en Parquet avec compression.
pyarrow.parquet.read_metadata(path) # Lire les métadonnées d’un fichier Parquet.

# 6. Lecture et écriture en batch

pyarrow.RecordBatchReader.from_batches(schema, batches) # Créer un lecteur de batchs.
pyarrow.RecordBatchWriter() # Écrire des batchs de données.

# 7. Interopérabilité et streaming

pyarrow.ipc.RecordBatchStreamWriter() # Écrire des données en flux (streaming).
pyarrow.ipc.RecordBatchStreamReader() # Lire des données en flux.


# Ces fonctions couvrent 90% des besoins pour PyArrow :

# Lecture/écriture optimisée (Parquet, Feather).
# Conversion rapide avec pandas.
# Manipulation en mémoire pour gros volumes.
