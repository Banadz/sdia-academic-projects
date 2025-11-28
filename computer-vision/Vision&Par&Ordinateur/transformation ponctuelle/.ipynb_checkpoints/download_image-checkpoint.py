from PIL import Image
import os

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


def sauvegarder_image(image, chemin_original):
    nom_fichier = os.path.splitext(os.path.basename(chemin_original))[0]
    nouveau_nom = f"inverse_{nom_fichier}.png"
    image.save(nouveau_nom)
    print(f"✅ Image sauvegardée sous : {nouveau_nom}")