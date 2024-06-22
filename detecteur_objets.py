import cv2
import numpy as np

# Définition de la classe DetecteurObjets pour la détection d'objets avec le modèle YOLO
class DetecteurObjets:
    # Chemins des fichiers de configuration, de poids et des classes du modèle YOLO
    CHEMIN_CONFIG_YOLO = 'yolov3.cfg'
    CHEMIN_POIDS_YOLO = 'yolov3.weights'
    CHEMIN_CLASSES_YOLO = 'coco.names'

    def __init__(self):
        # Initialisation du modèle YOLO
        print("Chargement du modèle YOLO...")
        self.net = cv2.dnn.readNet(self.CHEMIN_POIDS_YOLO, self.CHEMIN_CONFIG_YOLO)
        
        # Chargement des noms de classes depuis le fichier coco.names
        self.classes = []
        with open(self.CHEMIN_CLASSES_YOLO, 'r') as f:
            self.classes = [line.strip() for line in f.readlines()]
        
        # Récupération des noms des couches et des couches de sortie du modèle
        self.noms_couches = self.net.getLayerNames()
        self.couches_sorties = [self.noms_couches[i - 1] for i in self.net.getUnconnectedOutLayers()]
        
        # Définition des seuils de confiance et de non-maxima suppression (NMS)
        self.confidence_threshold = 0.5
        self.nms_threshold = 0.4
        print("Modèle YOLO chargé avec succès")

    def charger_image(self, chemin_image):
        # Chargement d'une image depuis le chemin spécifié
        print(f"Chargement de l'image : {chemin_image}")
        self.image = cv2.imread(chemin_image)
        if self.image is None:
            raise FileNotFoundError(f"Le fichier image '{chemin_image}' n'a pas pu être chargé. Vérifiez le chemin et l'intégrité du fichier.")
        self.hauteur, self.largeur, _ = self.image.shape

    def charger_video(self, chemin_video):
        # Chargement d'une vidéo depuis le chemin spécifié
        print(f"Chargement de la vidéo : {chemin_video}")
        self.cap = cv2.VideoCapture(chemin_video)
        if not self.cap.isOpened():
            raise FileNotFoundError(f"Le fichier vidéo '{chemin_video}' n'a pas pu être chargé. Vérifiez le chemin et l'intégrité du fichier.")

    def charger_webcam(self):
        # Ouverture de la webcam
        print("Ouverture de la webcam...")
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise RuntimeError("La webcam n'a pas pu être ouverte. Vérifiez la connexion de la webcam.")

    def detecter_objets(self, type_source='image'):
        # Détection des objets dans l'image ou la vidéo
        print(f"Détection des objets dans la {type_source}...")
        if type_source == 'image':
            blob = cv2.dnn.blobFromImage(self.image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
            self.net.setInput(blob)
            self.sorties = self.net.forward(self.couches_sorties)
            self._dessiner_boites(self.image)
        elif type_source == 'video':
            while self.cap.isOpened():
                ret, frame = self.cap.read()
                self.hauteur, self.largeur, _ = frame.shape
                if not ret:
                    break
                blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
                self.net.setInput(blob)
                self.sorties = self.net.forward(self.couches_sorties)
                self._dessiner_boites(frame)
                cv2.imshow("Video", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            self.cap.release()
            cv2.destroyAllWindows()
        print("Détection terminée")

    def _dessiner_boites(self, img):
        # Dessiner les boîtes de détection sur l'image ou le frame vidéo
        print("Dessiner les boîtes de détection...")
        boites = []
        confidences = []
        ids_classes = []
        for sortie in self.sorties:
            for detection in sortie:
                scores = detection[5:]
                id_classe = np.argmax(scores)
                confiance = scores[id_classe]
                if confiance > self.confidence_threshold:
                    centre_x = int(detection[0] * self.largeur)
                    centre_y = int(detection[1] * self.hauteur)
                    w = int(detection[2] * self.largeur)
                    h = int(detection[3] * self.hauteur)
                    x = int(centre_x - w / 2)
                    y = int(centre_y - h / 2)
                    boites.append([x, y, w, h])
                    confidences.append(float(confiance))
                    ids_classes.append(id_classe)
        
        print(f"Nombre de boîtes détectées avant NMS : {len(boites)}")
        indices = cv2.dnn.NMSBoxes(boites, confidences, self.confidence_threshold, self.nms_threshold)
        print(f"Nombre de boîtes après NMS : {len(indices)}")
        
        for i in indices:
            x, y, w, h = boites[i]
            label = f"{self.classes[ids_classes[i]]}"
            # Affiche les boîtes uniquement pour ces classes spécifiques
            if label in ["mouse", "laptop", "keyboard"]: 
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        print("Boîtes dessinées")