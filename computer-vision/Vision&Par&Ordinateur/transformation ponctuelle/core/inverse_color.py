from PIL import Image

def convertir_en_gris(image): # utilisant un méthode de pillow
    return image.convert("L")

def convertir_rgb_en_gris(image): # en utilisant la formule standard NTSC
    largeur, hauteur = image.size
    image_rgb = image.convert("RGB")
    pixels_rgb = image_rgb.load()

    # Créer une nouvelle image vide en niveaux de gris
    image_gris = Image.new("L", (largeur, hauteur))
    pixels_gris = image_gris.load()

    for x in range(largeur):
        for y in range(hauteur):
            r, g, b = pixels_rgb[x, y]
            # if option == "1":
            y_val = int((r + g + b) / 3) # selon moi
            # elif option == "2":
            # y_val = int(0.299 * r + 0.587 * g + 0.114 * b) # standard NTSC
            pixels_gris[x, y] = y_val

    return image_gris

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
