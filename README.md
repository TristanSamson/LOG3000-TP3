# LOG3000-TP3

L'objectif de ce projet est de mettre en place une calculatrice fonctionnelle, capable d'effectuer des opérations arithmétiques de base sur le navigateur.

La calculatrice supporte les quatre opérations arithmétiques de base que sont l'addition, la soustraction, la multiplication et la division. 

Les expressions supportées doivent être atomiques. Autrement dit, elles doivent être composées uniquement de deux nombres séparés par un opérateur. La calculatrice ne supporte pas les opérations composées ou mises l'une à la suite de l'autre. La calculatrice ne supporte pas non plus les nombres négatifs comme opérandes, mais les résultats négatifs sont permis.

## Identification de l'équipe

Équipe 27

- Camil Bisson (2277718)
- Tristan Samson (2264049)

## Installation

### Prérequis

Avant de procéder à l'installation de la calculatrice, vous devez avoir sur votre ordinateur les programmes suivants:

- Git
- Python 3
- Pip

Vous devez également posséder un compte sur la plateforme GitHub.

### Procédure

Les commandes de cette procédure sont destinées à être utilisées dans PowerShell sur Windows.

Vous devez commencer par cloner le dépôt sur votre ordinateur à l'emplacement désiré, puis entrer dans le dossier:

```powershell
git clone https://github.com/TristanSamson/LOG3000-TP3.git
cd LOG3000-TP3
```

Par la suite, vous devez créer un environnement virtuel et installer Flask à l'intérieur de celui-ci:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install Flask
```

## Structure du projet

- `templates/`: Répertoire contenant les gabarits utilisés par le serveur Flask pour générer l'interface de l'application.
- `static/`: Répertoire contenant les ressources servies statiquement par Flask au navigateur, notamment les feuilles CSS.
- `app.py`: Contrôleur permettant de recevoir et de traiter les requêtes HTTP.
- `tests/`: Tests automatisés des opérations, des expressions, des routes HTTP et du HTML rendu.
- `operators.py`: Fonctions utilitaires permettant d'effectuer les opérations mathématiques de la calculatrice.

## Utilisation

Pour démarrer l'application, exécutez la commande suivante:
```powershell
.\.venv\Scripts\python.exe app.py
```

L’application est ensuite accessible dans votre navigateur à l’adresse `http://127.0.0.1:5000`.

Une fois l'application lancée, vous pouvez commencer à inscrire votre opération mathématique en utilisant les boutons de chiffres qui sont affichés à l'écran. Les chiffres de 1 à 9 sont disposés dans une grille de 3 boutons par 3 boutons, tandis que le bouton 0 se situe en-dessous du 7. 

Les quatre boutons d'opérateurs, "+", "-", "*" et "/" se retrouvent quant à eux sur la dernière colonne.

Chaque bouton de chiffre ou d'opérateur appuyé ajoutera son chiffre ou son opérateur à l'écran. Une fois l'expression voulue saisie, appuyer sur le bouton "=" situé dans la rangée du bas affiche le résultat à l'écran. 

Pour réinitialiser l'écran, le bouton "C" (pour "Clear") est également disponible dans la rangée du bas.

En cas d'erreur, le message sera affiché dans l'écran de la calculatrice. Une erreur peut survenir, par exemple, lorsqu'une division par zéro est effectuée ou lorsqu'une expression invalide est transmise. 

Pour arrêter l'application, vous pouvez effectuer `Ctrl + C` dans le terminal sur lequel l'application a été démarrée.

## Tests

Les tests automatisés de l'application sont regroupés dans le répertoire `tests/`. Ils servent à vérifier le bon fonctionnement des opérations arithmétiques, la validation des expressions et le traitement des requêtes HTTP. Les cas testés couvrent les cas attendus, les cas limites et les cas hors limites.

Pour exécuter les tests unitaires, vous pouvez exécuter la commande suivante dans le terminal:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Les tests de l’interface vérifient le HTML rendu et les actions déclarées des boutons; ils n’exécutent pas JavaScript. Voir [la documentation des tests](tests/README.md) pour le détail de la couverture.

## Contribution

Le flux de contribution de ce projet est organisé à l'aide des *issues*, des branches et des *pull requests* disponibles sur la plateforme GitHub.

1. Pour chaque bogue découvert ou test échoué, créer une issue décrivant le problème et les étapes de reproduction et le test en échec, s'il y a lieu. Assigner l'issue à un membre de l'équipe de développement.
2. Un membre de l'équipe de développement créera une branche distincte pour cette issue, structurée de la manière suivante: `fix/<no. issue>/<court-descriptif>`. Par exemple: `fix/4/division-par-zero`.
3. Effectuer la correction sur cette branche et ajouter un test ciblé au besoin. Réexécuter les tests concernés et vérifier le bon fonctionnement du correctif. Consigner les résultats pour inclure plus tard dans la pull request.
4. Créer un ou plusieurs commits avec des messages clairs et explicites expliquant les correctifs appliqués, puis pousser la branche sur GitHub.
5. Ouvrir une pull request vers `main` en référençant l'issue réglée par la branche. Par exemple: `Closes #4`. Assigner un réviseur pour la pull request.
6. Le réviseur révise la pull request qui lui a été assignée en vérifiant que le correctif fonctionne, puis fusionne la branche.
7. Après la fusion, réexécuter toute la suite de tests, vérifier que le bogue a bien été résolu, puis confirmer que l'issue correspondante a bien été fermée.

Le processus est le même pour l'ajout de fonctionnalités, à la différence que le nom des branches doit commencer par `feat/`. L'ajout de nouvelles fonctionnalités doit également venir avec de nouveaux tests automatisés.

La documentation doit être mise à jour lorsque des modifications affectent l'installation, l'utilisation ou le fonctionnement du projet. Elle doit également être modifiée lorsque des changements au code modifient la véracité des commentaires qui y sont présents.