from PIL import Image
from core.lissage_conservateur import lister_voisin

def filtrage_median(image_org):
    largeur, hauteur = image_org.size
    pixels = image_org.load()

    # Créer une nouvelle image vide
    image_filtre = Image.new("L", (largeur, hauteur))
    pixels_filtre = image_filtre.load()

    for x in range(1, largeur - 1, 1):
        for y in range(1, hauteur - 1, 1):
            voisins = lister_voisin(pixels, x, y)
            voisins.sort()
            median = voisins[4]
# remplacer par mediane des voisins
            pixels_filtre[x, y] = median


    return image_filtre
