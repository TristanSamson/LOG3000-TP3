# Gabarits HTML

Ce répertoire contient les gabarits utilisés par le serveur Flask pour
générer les pages HTML de l'application.

Ces fichiers sont des gabarits puisque certaines parties de leur contenu sont
générées dynamiquement par le serveur.

## Fichiers et responsabilités

- `index.html`: Interface de la calculatrice. Contient l'écran, les boutons et
  les fonctions JavaScript permettant de contrôler le contenu de l'écran en y ajoutant des
  caractères ou en le réinitialisant.

## Dépendances, hypothèses et fonctionnement

- Le gabarit est rendu par la route `/` définie dans `app.py`, suite à une requête 
`GET` ou `POST`
- Utilise Jinja comme format de gabarit. La variable Jinja `result` contient le
résultat ou le message d'erreur à afficher provenant du serveur. 
- Le formulaire transmet l'expression inscrite à l'écran au serveur dans un champ 
`display` via une requête `POST` à la route `/`.
- Le style de la page dépend du fichier `static/style.css`, chargé via la fonction
Flask `url_for`.
- Nécessite l'utilisation de JavaScript pour faire fonctionner les boutons.