# Exercices pour la formation Python : TP2

Pour chaque exercice, ecrire les tests correspondant afin de valider votre développement.
De l'exercice 1 à 4 veuillez utiliser des fonctions simple puisque pas encore vue afin de tester facilement.

exemple de code:
```py
def my_func():
    # definition variable
    x = "var"
    return x
```

Pour chaque exercice, créez un fichier Python séparé ou regroupez-les dans un même fichier en commentant chaque section. Testez vos scripts et vérifiez leur bon fonctionnement.

## 1. Types de base
- Créez des variables de type entier, flottant, chaîne de caractères et booléen.
- Affichez leur type avec la fonction `type()`.

## 2. Types agrégés
Créez une liste (list), un tuple (tuple), un dictionnaire (dict) et un ensemble (set):
- liste: liste en entrée : [1, 2, 3], liste en sortie attendu : [0, 3, 4]
- tuple: tuple en entrée : (1, 2, 3), liste en sortie attendu : (1, 2, 3)
- dictionnaire: dict en entrée : {"a": 1, "b": 2}, dict en sortie attendu : {"a": 0, "c": 3}
- ensemble: dict en entrée : {1, 2, 3}, dict en sortie attendu : {1, 3, 4}

Effectuer des opérations sur chacun des types afin de répondre au entrée/sorties précédente

## 3. Context manager
- Utilisez un context manager (`with`) pour ouvrir un fichier en écriture, y écrire une ligne, puis le relire.

## 4. Instructions de base
- Écrivez un programme qui utilise des conditions (`if/else`), des boucles (`for`, `while`) et des instructions de contrôle (`break`, `continue`).
- condition: créer une variable x avec une condition si sup à 5 alors retourne "x est supérieur à 5\n" sinon retourne "x est inférieur ou égal à 5\n"
- boucle for: Créer une boucle for qui vas de 0 à 4 et evite le 3 résultat attendu : "0\n1\n2\n4\n"
- boucle while: Créer une boucle while qui vas de 0 à 4 et lorsqu'on arrive a 3 stoper la boucle

## 5. Fonctions
- Définissez une fonction qui prend deux arguments et retourne leur somme.
- Définissez une fonction avec un argument par défaut qui retourn par défaut "Bonjour tous le monde" ou "Bonjour valeur de l'argument" 
- Définissez une fonction avec un nombre variable d’arguments.

## 6. Import de module
- Importez le module `math` et utilisez au moins deux fonctions de ce module dans un script.

