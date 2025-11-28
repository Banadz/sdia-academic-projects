from PIL import Image

def lissage_conservateur(image_org):
    largeur, hauteur = image_org.size
    pixels = image_org.load()

    # Créer une nouvelle image vide
    image_lisse = Image.new("L", (largeur, hauteur))
    pixels_lisse = image_lisse.load()

    for x in range(1, largeur - 1, 1):
        for y in range(1, hauteur - 1, 1):
            val = pixels[x, y]
            voisins = lister_voisin(pixels, x, y)
            min_voisin = min(voisins)
            max_voisin = max(voisins)
            
# Rester dans la gamme
            if val > max_voisin:
                pixels_lisse[x, y] = max_voisin
            elif val < min_voisin:
                pixels_lisse[x, y] = min_voisin
            else:
                pixels_lisse[x, y] = val


    return image_lisse

def lister_voisin(pixels, i, j):
    array_voisin = []
    array_voisin = [
        pixels[i-1, j-1],
        pixels[i,   j-1],
        pixels[i+1, j-1],
        pixels[i-1, j],
        pixels[i+1, j],
        pixels[i-1, j+1],
        pixels[i,   j+1],
        pixels[i+1, j+1]
    ]
    return array_voisin