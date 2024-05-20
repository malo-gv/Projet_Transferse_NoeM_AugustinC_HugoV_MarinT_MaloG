# Jeu Bow Battle

## Description

Ce projet est un jeu de tir à l'arc développé en Python en utilisant la bibliothèque Pygame. Le but du jeu est de tirer des flèches sur une cible qui change de position après chaque tir réussi.

## Fonctionnalités

- **Calcul de la trajectoire de la flèche en fonction de l'angle de tir et de la force**
- **Affichage de la trajectoire prévue avant le tir**
- **Détection de collision entre la flèche et la cible**
- **Mouvement aléatoire de la cible après chaque tir réussi**
- **Indicateur de puissance pour montrer la force du tir en cours de chargement**

## Structure du projet

- `main.py` : Le fichier principal qui initialise le jeu et gère la boucle principale du jeu.
- `arrow.py` : Contient les fonctions pour gérer l'affichage et le mouvement de la flèche, ainsi que pour vérifier les collisions avec la cible.
- `constants.py` : Définit les constantes utilisées dans le jeu, comme les positions initiales, les dimensions de la fenêtre, et la gravité.
- `target.py` : Contient la fonction pour déplacer la cible à une nouvelle position aléatoire après chaque tir réussi.

## Prérequis

- Python 3.x
- Pygame

## Utilisation

1. Assurez-vous que les fichiers suivants sont dans le même répertoire :
    - `main.py`
    - `arrow.py`
    - `constants.py`
    - `target.py`
      
    - Les images nécessaires (dans les dossiers appropriés) :
        - `Images background/background v1.jpg`
        - `sprites character/archer.png`
        - `sprites character/arrow.png`
        - `sprites character/bullseye.png`

## Contrôles

- **Utilisation de la souris pour viser :** Le jeu calcule automatiquement l'angle de tir basé sur la position de la souris.
- **Maintenez la touche `Espace` pour charger la puissance du tir :** Relâchez la touche `Espace` pour tirer la flèche.
