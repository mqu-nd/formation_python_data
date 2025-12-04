# Exercices pour la formation Python : TP2

Pour chaque exercice, ecrire les tests correspondant afin de valider votre développement.

Prenons un cas de jeux vidéo avec des personnages que nous pouvons incarner.

## Premiere classe :

Dans le cadre d'un premier exercice écrivez un programme Python simple en suivante les instructions suivantes : 

1. Créer une classe Personnage avec les attributs suivants : 
- `nom` (le nom du personnage)
- `niveau` (le niveau du personnage, initialisé à 1 par défaut)
- `points_vie` (les points de vie, initialisés à 100 par défaut)

2. Ajouter les méthodes suivantes
- `attaquer()` : affiche "Le personnage attaque" et retourne 10 points de dégâts
- `recevoir_degats(degats)` : réduit les points de vie du personnage
- `__str__(self)` : retourne une représentation textuelle de l'objet (ex : "Gandalf (PV: 80, Niveau: 5)")

Testez votre classe en créant un personnage, en lui faisant subir des dégâts et en affichant ses informations.

## Héritage & Polymorphisme

Reprenez le cas des personnages et faisons en sorte d'avoir plusieurs type de personnage. Pour ce faire ici écrivez un programme Python en suivant les instructions suivantes :

1. Créer une classe mère `Personnage` avec :
   - Un attribut `nom`
   - Un attribut `niveau`
   - Un attribut `points_vie`
   - Une méthode `attaquer()` qui affiche "Le personnage attaque"
   - Une méthode `recevoir_degats(degats)` qui réduit les points de vie

2. Créer une classe `Guerrier` qui hérite de `Personnage` avec :
   - Un attribut supplémentaire `force`
   - Redéfinir `attaquer()` pour afficher "Le guerrier charge avec son épée"
   - Une méthode `coup_critique()` qui inflige des dégâts doublés

3. Créer une classe `Mage` qui hérite de `Personnage` avec :
   - Un attribut supplémentaire `mana`
   - Redéfinir `attaquer()` pour afficher "Le mage lance un sort"
   - Une méthode `lancer_sort(nom_sort, cout_mana)` qui consomme du mana, la valeur du cout mana doit etre spécifié par défaut à 20 pour avoir un mini de consommation

4. Tester l'héritage en créant des instances de `Guerrier` et `Mage` et en simulant un combat. 

## Abstraction 

En reprenant le sujet précédent adapter votre code afin d'y intégrer la notion de classe abstraite.

## Interface

Même exercice que l'abstraction mais pour l'interface.