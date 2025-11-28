from download_image import choisir_image, sauvegarder_image
from inverse_color import convertir_en_gris, inverser_niveaux_de_gris


def main():
    chemin_image = choisir_image()
    if not chemin_image:
        return

    try:
        with Image.open(chemin_image) as img:
            image_gris = convertir_en_gris(img)
            image_inverse = inverser_niveaux_de_gris(image_gris)
            sauvegarder_image(image_inverse, chemin_image)
    except Exception as e:
        print(f"❌ Erreur pendant le traitement de l'image : {e}")

if __name__ == "__main__":
    main()