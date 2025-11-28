from PIL import Image
from interface.home import App
from core.download_image import choisir_image, sauvegarder_image
from core.inverse_color import convertir_en_gris, convertir_rgb_en_gris, inverser_niveaux_de_gris
import tkinter as tk

# def main():
#     chemin_image = choisir_image()
#     if not chemin_image:
#         return

#     try:
#         with Image.open(chemin_image) as img:
#             # image_gris = convertir_en_gris(img)
#             image_gris = convertir_rgb_en_gris(img)
#             sauvegarder_image(image_gris, chemin_image, "nuance_de_gris")
#             image_inverse = inverser_niveaux_de_gris(image_gris)
#             sauvegarder_image(image_inverse, chemin_image, "inversion_niveaux_de_gris")
#     except Exception as e:
#         print(f"❌ Erreur pendant le traitement de l'image : {e}")

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()