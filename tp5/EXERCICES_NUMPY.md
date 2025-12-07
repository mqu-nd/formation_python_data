[[__TOC__]]

# Exercices pour la formation Python : TP5 

Rappel pour s'assurer d'avoir toutes les librairies nécessaires pour le TP:
```sh
pip install -r requirements.txt
```

# Numpy 

## Fonction utile pour le TP :

```python
import numpy as np

# Fonction utile pour la résolution des exercices :
np.arange(12)    # Création d'un tableau 1D de 0 à 11 ex : [0 1 2 3 4 5 6 7 8 9 10 11]
np.zeros((3,4))  # Création d'un tableau 2D de 3x4 rempli de zéros
np.ones((2,3))   # Création d'un tableau 2D de 2x3 rempli de uns
np.linspace(0,10,5)  # Création de 5 valeurs équidistantes entre 0 et 10
np.reshape(arr, (3,4))  # Redimensionnement d'un array en forme 3x4
np.array([1,2,3])  # Création d'un array à partir d'une liste
np.random.randn(3,3)  # Génération d'un array 3x3 de nombres aléatoires normaux
np.tile(arr, 3)  # Répétition d'un array 3 fois
np.concatenate([arr1, arr2])  # Concaténation de deux arrays
np.sum(arr, axis=0)  # Somme le long de l'axe 0 (colonnes)
np.sum(arr, axis=1)  # Somme le long de l'axe 0 (lignes)
np.mean(arr)     # Calcul de la moyenne
np.max(arr)      # Valeur maximale
np.where(arr > 5)  # Indices où la condition est vraie
np.argsort(arr_unsorted) # Indices qui trieraient l'array
arr.shape        # Forme de l'array ex: (3, 4) pour une matrice 3x4
arr.dtype        # Type de données de l'array (int64, float64, etc.) 
arr.flatten()    # Aplatissement en 1D
arr.T            # Transposition

# Fonction utile pour faire vos assertions :
assert np.array_equal(np.array([1,2,3]), np.array([1,2,3]))
assert np.allclose(np.array([1.0,2.0,3.0]), np.array([1.0,2.0,3.0]))   
```

Voici les fixtures NumPy disponibles pour vos tests :

```python
@pytest.fixture
def array_simple():
    """Array 1D simple pour les tests de base"""
    return np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

@pytest.fixture
def array_2d():
    """Array 2D pour les tests de manipulation"""
    return np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

@pytest.fixture
def array_random():
    """Array avec valeurs aléatoires reproductibles"""
    np.random.seed(42)
    return np.random.randn(5, 4)

def test_demo_numpy(array_simple):
    assert array_simple.shape == (10,)
    assert array_simple.dtype == np.int64
```

### Exercice 1 : Création et manipulation de base d'arrays

1. **Création d'arrays** :
   - Créez un array 1D contenant les nombres de 0 à 9
   - Créez un array 2D de forme (3, 4) rempli de zéros
   - Créez un array 2D de forme (2, 3) rempli de uns
   - Créez un array contenant une séquence de 0 à 20 avec un pas de 2

2. **Propriétés des arrays** :
   - Affichez la forme, la dimension, le type de données et la taille d'un array

3. **Indexation et slicing** :
   - Accédez au 3ème élément d'un array 1D
   - Accédez à l'élément en position (1, 2) d'un array 2D
   - Extrayez les 5 premiers éléments d'un array
   - Extrayez une sous-matrice d'un array 2D

### Exercice 2 : Opérations mathématiques et broadcasting

1. **Opérations élément par élément** :
   - Créez deux arrays et effectuez les opérations : addition, soustraction, multiplication, division
   - Calculez la racine carrée, l'exponentielle et le logarithme d'un array
   - Trouvez le minimum, maximum, somme et moyenne d'un array

2. **Broadcasting** :
   - Ajoutez un scalaire à un array
   - Multipliez un array 2D par un array 1D
   - Démontrez le broadcasting avec des arrays de formes différentes

3. **Opérations sur les axes** :
   - Calculez la somme par ligne et par colonne d'une matrice
   - Trouvez l'index du maximum par ligne

### Exercice 3 : Reshape et manipulation de forme

1. **Redimensionnement** :
   - Transformez un array 1D de 12 éléments en matrice 3x4
   - Aplatissez une matrice 2D en array 1D
   - Transposez une matrice

2. **Concaténation et division** :
   - Concaténez deux arrays horizontalement et verticalement
   - Divisez un array en plusieurs sous-arrays
   - Empilez des arrays

3. **Manipulation avancée** :
   - Répétez un array plusieurs fois
   - Inversez l'ordre des éléments
   - Triez un array

### Pour allez plus loin :

### Exercice 4 : Indexation avancée et masquage

1. **Indexation booléenne** :
   - Filtrez les éléments d'un array selon une condition
   - Remplacez tous les éléments négatifs par zéro
   - Trouvez les indices des éléments satisfaisant une condition

2. **Indexation avec des arrays d'indices** :
   - Sélectionnez des éléments spécifiques avec un array d'indices
   - Utilisez `np.where` pour une sélection conditionnelle
   - Implémentez une sélection complexe avec plusieurs conditions

3. **Masquage** :
   - Créez un masque pour identifier les valeurs manquantes
   - Appliquez un masque pour filtrer des données
   - Combinez plusieurs masques avec des opérations logiques

### Exercice 5 : Fonctions statistiques et agrégation

1. **Statistiques descriptives** :
   - Calculez la moyenne, médiane, écart-type et variance
   - Trouvez les percentiles et quartiles
   - Calculez la corrélation entre deux arrays

2. **Agrégation conditionnelle** :
   - Calculez la somme des éléments positifs
   - Trouvez la moyenne des valeurs supérieures à un seuil
   - Comptez le nombre d'éléments satisfaisant une condition

3. **Opérations par groupe** :
   - Groupez des données et calculez des statistiques par groupe
   - Utilisez `np.bincount` pour compter les occurrences
   - Implémentez une fonction d'agrégation personnalisée

### Exercice 6 : Génération de nombres aléatoires

1. **Nombres aléatoires de base** :
   - Générez des nombres aléatoires uniformes et normaux
   - Créez des échantillons aléatoires à partir d'une distribution
   - Mélangez aléatoirement un array

2. **Distributions statistiques** :
   - Générez des données suivant différentes distributions (binomiale, Poisson, etc.)
   - Créez des données de test avec des propriétés statistiques spécifiques
   - Simulez des processus stochastiques simples

3. **Échantillonnage** :
   - Échantillonnez avec et sans remise
   - Créez des échantillons stratifiés
   - Générez des permutations aléatoires

### Exercice 7 : Manipulation de données réelles

1. **Données temporelles** :
   - Générez une série temporelle avec `np.datetime64`
   - Calculez des moyennes mobiles
   - Détectez des tendances et saisonnalités

2. **Données d'images** :
   - Manipulez des images représentées par des arrays 3D
   - Appliquez des filtres simples (flou, contours)
   - Redimensionnez et faites des rotations d'images

3. **Données scientifiques** :
   - Simulez des données expérimentales avec du bruit
   - Calculez des histogrammes et distributions
   - Ajustez des courbes à des données

### Conseils pour la résolution

- Utilisez `np.info()` pour obtenir de l'aide sur les fonctions NumPy
- Testez vos solutions étape par étape avec de petits arrays
- Privilégiez la vectorisation plutôt que les boucles
- Vérifiez toujours la forme et le type de vos arrays
- Utilisez `%timeit` en Jupyter pour mesurer les performances

### Ressources utiles

- [Documentation officielle NumPy](https://numpy.org/doc/stable/)
- [NumPy Quickstart Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
- [NumPy for MATLAB users](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html)
- [Array Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html) 
