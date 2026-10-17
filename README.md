# LOG3000-TP3

L'objectif de ce projet est de mettre en place une calculatrice fonctionnelle, capable d'effectuer des opérations arithmétiques de base sur le navigateur.

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

Enfin, vous pouvez démarrer l'application:
```powershell
.\.venv\Scripts\python.exe app.py
```

L’application est ensuite accessible dans votre navigateur à l’adresse `http://127.0.0.1:5000`.

Pour arrêter l'application, vous pouvez effectuer `Ctrl + C` dans le terminal sur lequel l'application a été démarrée.

