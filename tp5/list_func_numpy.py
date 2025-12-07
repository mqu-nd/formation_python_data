import numpy as np

# 1. Création de tableaux

arr = np.array() # Créer un tableau à partir d’une liste ou d’un tuple.
np.zeros() # Créer un tableau rempli de zéros.
np.ones() # Créer un tableau rempli de uns.
np.arange() # Créer une séquence (comme range mais en tableau NumPy).
np.linspace() # Créer une séquence avec un nombre fixe de points entre deux bornes.
np.eye() # Créer une matrice identité.


# 2. Exploration et propriétés

arr.shape # Dimensions du tableau.
arr.ndim # Nombre de dimensions.
arr.size # Nombre total d’éléments.
arr.dtype # Type des éléments.
np.reshape() # Changer la forme du tableau.


# 3. Opérations mathématiques

np.sum() # Somme des éléments.
np.mean() # Moyenne.
np.std() # Écart-type.
np.min() / np.max() # Minimum / Maximum.
np.prod() # Produit des éléments.
np.cumsum() # Somme cumulée.
np.diff() # Différences entre éléments consécutifs.


# 4. Opérations vectorisées

np.add(), np.subtract(), np.multiply(), np.divide() # Opérations élément par élément.
np.power() # Puissance.
np.sqrt() # Racine carrée.
np.exp() # Exponentielle.
np.log() # Logarithme.


# 5. Indexation et filtrage

arr[mask] # Filtrage avec masque booléen.
np.where() # Retourne les indices où la condition est vraie.
np.take() # Sélection par indices.


# 6. Génération aléatoire

np.random.rand() # Nombres aléatoires uniformes.
np.random.randn() # Nombres aléatoires suivant une loi normale.
np.random.randint() # Entiers aléatoires.
np.random.choice() # Tirage aléatoire dans un tableau.


# 7. Algèbre linéaire

np.dot() # Produit scalaire ou matriciel.
np.matmul() # Multiplication matricielle.
np.linalg.inv() # Inverse d’une matrice.
np.linalg.det() # Déterminant.
np.linalg.eig() # Valeurs propres et vecteurs propres.