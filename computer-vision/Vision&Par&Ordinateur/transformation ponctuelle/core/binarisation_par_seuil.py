from PIL import Image
import numpy as np

def binarisation_par_seuil(image_org):
    histo = calcul_histograme(image_org)
    seuil = seuil_optimal(histo)

    largeur, hauteur = image_org.size
    pixels = image_org.load()

    # Créer une nouvelle image vide
    image_binaire = Image.new("1", (largeur, hauteur))
    pixels_binaire = image_binaire.load()

    for x in range(largeur):
        for y in range(hauteur):
            val = pixels[x, y]
            if val >= seuil:
                pixels_binaire[x, y] = 255  # blanc
            else:
                pixels_binaire[x, y] = 0  # noir

    return image_binaire

def calcul_histograme(image):
    histo = image.histogram()[:256]
    return histo

def seuil_optimal(H):
    S = 0
    min_cout = cout_otsu(H, 0)
    for i in range(1, 256):
        cout = cout_otsu(H, i)
        if cout < min_cout:
            min_cout = cout
            S = i
    return S

def cout_otsu(H, seuil):
    total = sum(H)
    if total == 0:
        return float("inf")

    # Probas cumulées
    w0 = sum(H[:seuil]) / total
    w1 = sum(H[seuil:]) / total

    if w0 == 0 or w1 == 0:
        return float("inf")

    # Moyennes cumulées
    mu0 = sum(i * H[i] for i in range(seuil)) / sum(H[:seuil])
    mu1 = sum(i * H[i] for i in range(seuil, 256)) / sum(H[seuil:])

    # Variance intra-classe
    variance_intra = w0 * w1 * (mu0 - mu1) ** 2
    return -variance_intra