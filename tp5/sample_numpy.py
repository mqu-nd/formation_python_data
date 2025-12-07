import numpy as np
# Création d'un tableau NumPy à partir d'une liste Python
arr = np.array([10, 20, 30, 40, 50])
print(arr)

# Calculs statistiques
print("Somme :", np.sum(arr))
print("Moyenne :", np.mean(arr))
print("Écart-type :", np.std(arr))

# Opérations vectorielles (ajout de 5 à chaque élément)
arr_plus_5 = arr + 5
print("Tableau + 5 :", arr_plus_5)

# Racine carrée de chaque élément
print("Racine carrée :", np.sqrt(arr))
