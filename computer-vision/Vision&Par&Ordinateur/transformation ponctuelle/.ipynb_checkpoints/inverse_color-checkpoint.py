from PIL import Image

def convertir_en_gris(image):
    # Convertir en niveaux de gris (mode "L")
    return image.convert("L")

def inverser_niveaux_de_gris(image_gris):
    largeur, hauteur = image_gris.size
    pixels = image_gris.load()

    # Créer une nouvelle image vide
    image_inverse = Image.new("L", (largeur, hauteur))
    pixels_inverse = image_inverse.load()

    for x in range(largeur):
        for y in range(hauteur):
            val = pixels[x, y]
            pixels_inverse[x, y] = 255 - val

    return image_inverse
