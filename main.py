from detecteur_objets import DetecteurObjets
from utils import afficher_image, afficher_video

# Point d'entrée principal du script
if __name__ == "__main__":
    # Création d'une instance de la classe DetecteurObjets
    detecteur = DetecteurObjets()
    
    try:
        # Détection d'objets dans une image
        detecteur.charger_image("souris.jpeg")  
        detecteur.detecter_objets('image')
        afficher_image(detecteur.image)
    except FileNotFoundError as e:
        # Gestion de l'erreur si le fichier image n'est pas trouvé
        print(e)
    
    try:
        # Détection d'objets dans un flux vidéo de la webcam
        detecteur.charger_webcam()
        detecteur.detecter_objets('video')
        afficher_video(detecteur.cap)
    except RuntimeError as e:
        # Gestion de l'erreur si la webcam ne peut pas être ouverte
        print(e)