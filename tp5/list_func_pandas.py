import pandas as pd
from pandas import DataFrame

# 1. Chargement et export des données

pd.read_csv() # Lire un fichier CSV.
pd.read_excel() # Lire un fichier Excel.
pd.read_sql() # Charger depuis une base SQL.
pd.read_parquet() # Lire un fichier Parquet.
DataFrame.to_csv() # Exporter en CSV.
DataFrame.to_parquet() # Exporter en Parquet.


# 2. Exploration des données

df.head() # Afficher les premières lignes.
df.tail() # Afficher les dernières lignes.
df.info() # Informations sur les colonnes et types.
df.describe() # Statistiques descriptives.
df.shape # Dimensions (lignes, colonnes).
df.columns # Liste des colonnes.
df.dtypes # Types des colonnes.


# 3. Sélection et filtrage

df['colonne'] # Sélection d’une colonne.
df[['col1', 'col2']] # Sélection multiple.
df.loc[] # Sélection par labels.
df.iloc[] # Sélection par index.
df.query("Age > 30") # Filtrage avec une expression.


# 4. Nettoyage et transformation

df.drop(columns=['colonne']) # Supprimer une colonne.
df.rename(columns={'old': 'new'}) # Renommer colonnes.
df.fillna('valeur') # Remplacer les valeurs manquantes.
df.dropna() # Supprimer les lignes avec NaN.
df.astype({'colonne': 'int'}) # Changer le type.
df['colonne'].str.strip() # Nettoyer les espaces.


# 5. Agrégation et regroupement

df.groupby('colonne').mean() # Moyenne par groupe.
df.groupby(['col1', 'col2']).agg({'col3': 'sum'}) # Agrégation personnalisée.
df.value_counts() # Compter les occurrences.


# 6. Tri et réindexation

df.sort_values('colonne') # Trier par colonne.
df.reset_index(drop=True) # Réinitialiser l’index.


# 7. Fusion et jointure

pd.merge(df1, df2, on='colonne') # Jointure SQL-like.
pd.concat([df1, df2]) # Concaténation verticale ou horizontale.


# 8. Opérations avancées

df.apply(func) # Appliquer une fonction à chaque ligne/colonne.
df.map(func) # Appliquer une fonction sur une série.
df.pivot_table() # Table pivot.
df.melt() # Transformer en format long.