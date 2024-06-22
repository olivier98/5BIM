# Projet de Détection d'Objets : Ordinateurs et Souris

## Description

Ce projet implémente un système de détection d'ordinateurs et de souris dans des images ou des flux vidéo en utilisant OpenCV et le modèle de détection d'objets YOLO (You Only Look Once). Le projet est réalisé en suivant une approche de programmation orientée objet (POO) et le code est bien commenté pour en expliquer les fonctionnalités et la logique.

## Fonctionnalités

- Chargement et affichage d'images et de vidéos.
- Détection des objets spécifiques (ordinateurs, souris) dans des images et des flux vidéo.
- Utilisation de YOLO pour la détection d'objets.
- Intégration des concepts de POO.
- Affichage des résultats de détection.

## Prérequis

- Python 3.6 ou supérieur
- OpenCV 4.5 ou supérieur
- YOLOv3 ou une version ultérieure

## Installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/olivier98/5BIM/
    cd 5BIM
    ```

2. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

3. Téléchargez les fichiers de configuration et les poids de YOLO : `yolov3.weights à télécharger`
    - [yolov3.cfg](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg)
    - [yolov3.weights](https://pjreddie.com/media/files/yolov3.weights)
    - [coco.names](https://github.com/pjreddie/darknet/blob/master/data/coco.names)

4. Placez les fichiers téléchargés dans le répertoire du projet.

## Utilisation

### Détection dans une image

1. Placez l'image que vous souhaitez analyser dans le répertoire du projet.
2. Modifiez le fichier `main.py` pour spécifier le chemin de l'image.
3. Exécutez le script :
    ```bash
    python main.py
    ```

### Détection dans un flux vidéo (webcam)

1. Assurez-vous que votre webcam est connectée et fonctionne correctement.
2. Exécutez le script :
    ```bash
    python main.py
    ```

## Structure du Projet

- `detecteur_objets.py` : Contient la classe `DetecteurObjets` pour la détection d'objets en utilisant YOLO.
- `utils.py` : Contient des fonctions utilitaires pour afficher des images et des vidéos.
- `main.py` : Point d'entrée principal du script, gère la détection d'objets dans les images et les vidéos.
- `requirements.txt` : Liste des dépendances Python nécessaires pour exécuter le projet.

## Auteurs

- Votre Nom - [olivier98](https://github.com/olivier98/)

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Remerciements

- [YOLO - You Only Look Once](https://pjreddie.com/darknet/yolo/)
- [OpenCV](https://opencv.org/)