from PIL import Image
from core.lissage_conservateur import lister_voisin

def filtrage_lineaire(image_org, filtre):
    largeur, hauteur = image_org.size
    pixels = image_org.load()

    # Créer une nouvelle image vide
    image_filtre = Image.new("L", (largeur, hauteur))
    pixels_filtre = image_filtre.load()

    v_filtre = len(filtre[0])
    h_filtre = len(filtre)
    
    offset_x = v_filtre // 2
    offset_y = h_filtre // 2

    for x in range(offset_x, largeur - offset_x):
        for y in range(offset_y, hauteur - offset_y):
            valeur = 0
            for i in range(-offset_x, offset_x + 1):
                for j in range(-offset_y, offset_y + 1):
                    px = pixels[x + i, y + j]
                    coeff = filtre[j + offset_y][i + offset_x]
                    valeur += px * coeff

            
            pixels_filtre[x, y] = int(valeur)
            


    return image_filtre
