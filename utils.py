import cv2

# Ceci est une fonction pour afficher une image
def afficher_image(image):
    # Afficher l'image dans une fenêtre nommée "Image"
    cv2.imshow("Image", image)
    # Attendre une pression de touche pour fermer la fenêtre
    cv2.waitKey(0)
    # Détruire toutes les fenêtres ouvertes par OpenCV
    cv2.destroyAllWindows()

# Fonction pour afficher une vidéo
def afficher_video(cap):
    # Lire et afficher les frames de la vidéo tant que la vidéo est ouverte
    while cap.isOpened():
        # Lire une frame de la vidéo
        ret, frame = cap.read()
        if not ret:
            break
        # Afficher la frame dans une fenêtre nommée "Video"
        cv2.imshow("Video", frame)
        # Attendre 1 ms et vérifier si la touche 'q' est pressée pour arrêter la lecture
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Libérer l'objet vidéo
    cap.release()
    # Détruire toutes les fenêtres ouvertes par OpenCV
    cv2.destroyAllWindows()