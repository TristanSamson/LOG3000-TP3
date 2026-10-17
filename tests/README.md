# Tests automatisés

Ce répertoire permet de vérifier de manière automatisée le comportement attendu de la calculatrice grâce à plusieurs suites de tests.

## Fichiers et responsabilités

- `test_operators.py` : teste les quatre opérations, notamment les nombres décimaux, les résultats négatifs et la division par zéro.
- `test_app.py` : teste le calcul des expressions, la gestion des espaces, la validation du format et les erreurs.
- `test_routes.py` : teste les requêtes GET et POST, les résultats, les erreurs et la transmission du formulaire.
- `test_interface.py` : teste les libellés des chiffres et opérateurs, les actions déclarées des boutons et le formulaire.

## Exécution et dépendances

Se référer à la section "Tests" du README.md principal (`../README.md`)

## Portée et hypothèses

- Les opérandes négatifs sont refusés, mais les résultats négatifs sont permis.
- Les nombres flottants sont comparés avec une tolérance pour gérer leurs imprécisions de représentation.
- Les tests HTTP examinent aussi les variables envoyées au gabarit pour vérifier les résultats.
- Les tests de l'interface analysent le HTML rendu et les actions déclarées : ils ne simulent pas les clics et n'exécutent pas JavaScript. Le fonctionnement des interactions et le rendu CSS doivent également être vérifiés dans un navigateur.