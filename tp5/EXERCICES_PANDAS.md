[[__TOC__]]

# Exercices pour la formation Python : TP5 

Rappel pour s'assurer d'avoir toutes les librairies nécessaires pour le TP:
```sh
pip install -r requirements.txt
```

## Pandas

Dans le cadre de ce TP, vous avez la possibilité d'utiliser jupyter pour la réalisation.
Ou bien écrire directement dans vos tests.

Voici les dataframes d'entrée pour les exercices. Je vous fournis les fixtures pour le faire dans les tests directement avec un exemple de test qui l'utilise.
```python
@pytest.fixture
def df_simple() -> DataFrame:
    """ Dataframe simple pour les tests """
    return DataFrame({
        'nom': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'age': [25, 30, 35, 28, 22],
        'salaire': [50000, 60000, 75000, 55000, 48000],
        'departement': ['IT', 'RH', 'IT', 'Marketing', 'RH']
    })

@pytest.fixture
def df_to_clean() -> DataFrame:
    """ Dataframe avec des données manquantes pour les tests de nettoyage """
    return DataFrame({
        'nom': ['Alice', 'Bob', None, 'Diana', 'Eve', 'Frank'],
        'age': [25, 30, 35, np.nan, 22, 40],
        'salaire': [50000, np.nan, 75000, 55000, 48000, 62000],
        'email': ['alice@email.com', 'bob@email.com', 'charlie@email.com', None, 'eve@email.com', 'frank@email.com']
    })

    
    def test_demo(df_simple: DataFrame):
        assert not df_simple.empty
```

### Exercice 1 : Création et manipulation de base d'un DataFrame

1. Créez un DataFrame avec les données suivantes :
   ```python
   data = {
       'nom': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
       'age': [25, 30, 35, 28, 22],
       'salaire': [50000, 60000, 75000, 55000, 48000],
       'departement': ['IT', 'RH', 'IT', 'Marketing', 'RH']
   }
   ```

2. Affichez :
   - Les 3 premières lignes
   - Les informations sur le DataFrame (types de données, nombre de lignes, etc.)
   - Les statistiques descriptives pour les colonnes numériques
   - Les noms des colonnes

3. Ajoutez une nouvelle colonne 'bonus' qui représente 10% du salaire

### Exercice 2 : Filtrage et sélection

En utilisant le DataFrame de l'exercice 1 :

1. Sélectionnez uniquement les colonnes 'nom' et 'salaire'
2. Filtrez les employés qui ont plus de 25 ans
3. Trouvez les employés du département IT avec un salaire supérieur à 55000
4. Affichez les employés triés par salaire décroissant
5. Trouvez l'employé avec le salaire le plus élevé

### Exercice 3 : Opérations sur les groupes

1. Calculez le salaire moyen par département
2. Trouvez l'âge minimum et maximum par département
3. Comptez le nombre d'employés par département
4. Calculez le salaire total par département

### Exercice 4 : Manipulation de fichiers

1. Créez un fichier CSV avec les données de l'exercice 1
2. Lisez le fichier CSV dans un nouveau DataFrame
3. Ajoutez 5 nouveaux employés avec des données de votre choix
4. Sauvegardez le DataFrame modifié dans un nouveau fichier CSV

### Exercice 5 : Nettoyage de données

Créez un DataFrame avec des données manquantes :
```python
import numpy as np
data_messy = {
    'nom': ['Alice', 'Bob', None, 'Diana', 'Eve', 'John'],
    'age': [25, 30, 35, np.nan, 22, 40],
    'salaire': [50000, np.nan, 75000, 55000, 48000, 62000],
    'email': ['alice@email.com', 'bob@email.com', 'charlie@email.com', None, 'eve@email.com', 'John@email.com']
}
```

Tâches :
1. Identifiez les valeurs manquantes dans chaque colonne
2. Remplacez les âges manquants par l'âge moyen
3. Supprimez les lignes où le nom est manquant
4. Remplacez les salaires manquants par la médiane des salaires
5. Remplacez les emails manquants par 'email_manquant@company.com'

### Exercice 6 : Fusion de DataFrames

Créez deux DataFrames :
```python
# DataFrame des employés
employes = pd.DataFrame({
    'id_employe': [1, 2, 3, 4, 5],
    'nom': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'departement_id': [1, 2, 1, 3, 2]
})

# DataFrame des départements
departements = pd.DataFrame({
    'departement_id': [1, 2, 3, 4],
    'nom_departement': ['IT', 'RH', 'Marketing', 'Finance'],
    'budget': [100000, 80000, 90000, 120000]
})
```

Tâches :
1. Effectuez un inner join entre les deux DataFrames
2. Effectuez un left join pour garder tous les employés
3. Effectuez un right join pour garder tous les départements
4. Identifiez les départements sans employés

## Ressources utiles

- [Documentation officielle Pandas](https://pandas.pydata.org/docs/)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- Utilisez `help()` ou `?` dans Jupyter pour obtenir de l'aide sur les fonctions
