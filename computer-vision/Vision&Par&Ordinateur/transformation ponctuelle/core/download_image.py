from PIL import Image
import os
from datetime import datetime

def choisir_image():
    chemin = input("Entrez le chemin de l'image (jpg, png, etc.) : ").strip()
    if not os.path.exists(chemin):
        print("❌ Le fichier n'existe pas.")
        return None
    try:
        with Image.open(chemin) as img:
            img.verify()
        return chemin
    except Exception as e:
        print(f"❌ Erreur lors de l'ouverture de l'image : {e}")
        return None

def sauvegarder_image(image, chemin_original, operation):
    nom_fichier = os.path.splitext(os.path.basename(chemin_original))[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nouveau_nom = f"{timestamp}_{operation}_{nom_fichier}.png"
    chemin_sortie = os.path.join("result", nouveau_nom)
    image.save(chemin_sortie)
    print(f"✅ Image sauvegardée sous : /result/{nouveau_nom}")