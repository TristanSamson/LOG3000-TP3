# Ressources statiques

Ce répertoire contient les ressources servies statiquement, directement au navigateur
par le serveur Flask, notamment les styles de l'application et les images, s'il y a
lieu.

## Fichiers et responsabilités:

- `style.css` : définit l'apparence de la calculatrice, la disposition
  des boutons en quatre colonnes et leur visuel au survol et au clic.

## Dépendances, hypothèses et fonctionnement

- La feuille de styles CSS (*stylesheet*) `style.css` est importée et chargée par le
  gabarit `templates/index.html`.
- Les sélecteurs CSS dépendent des classes (`.class`) et identifiants (`#id`) définis
  dans le gabarit.
- La disposition des éléments utilise Flexbox et CSS Grid. Ces deux standards sont
  fonctionnels dans tous les navigateurs modernes.