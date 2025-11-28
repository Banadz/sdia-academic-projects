import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import os
import sys

sys.path.append(os.path.abspath(".."))

from core.inverse_color import inverser_niveaux_de_gris, convertir_rgb_en_gris
from core.download_image import sauvegarder_image
from core.lissage_conservateur import lissage_conservateur
from core.filtrage_median import filtrage_median
from core.convolution_discrete import filtrage_lineaire
from core.binarisation_par_seuil import binarisation_par_seuil

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Traitement d'Image")
        self.root.geometry("1080x720")
        self.image_originale = None
        self.image_gris = None
        self.image_inverse = None
        self.image_lisse_cons = None
        self.image_filtre_median = None
        self.image_convolution = None
        self.image_binarise = None
        self.image_result = None


        menu_bar = tk.Menu(root)

        menu_fichier = tk.Menu(menu_bar, tearoff=0)
        menu_fichier.add_command(label="Ouvrir un image", command=self.ouvrir_image)
        menu_fichier.add_command(label="Sauvegarder", command=self.sauvegarder_image)
        # menu_fichier.add_separator()
        menu_fichier.add_command(label="Quitter", command=self.quitter)

        menu_bar.add_cascade(label="Fichier", menu=menu_fichier)

        menu_aide = tk.Menu(menu_bar, tearoff=0)
        menu_aide.add_command(label="À propos", command=self.quitter)
        menu_bar.add_cascade(label="Aide", menu=menu_aide)

        self.root.config(menu=menu_bar)

        header = tk.Frame(root, bg="#074468", pady=20)
        header.pack(fill="x")

        self.canvas = tk.Label(self.root)
        self.canvas.pack(pady=10)

        # Footer
        footer = tk.Frame(root, bg="#eee", height=60)
        footer.pack(side="bottom", fill="x")

        # Contenu du footer
        btn_gris = tk.Button(footer, text="Nuance de gris", command=self.en_gris)
        btn_inverser = tk.Button(footer, text="Inverser", command=self.inverser)
        btn_lisasage_con = tk.Button(footer, text="Lissage conservateur", command=self.lissage_conservateur)
        btn_filtrage_median = tk.Button(footer, text="Filtrage médiane", command=self.filtrage_median)
        btn_filtrage_lineaire = tk.Button(footer, text="Filtrage linéaire", command=self.conolution)
        btn_binariser = tk.Button(footer, text="Binariser", command=self.binariser)
        btn_quitter = tk.Button(footer, text="Quitter", command=self.quitter)

        btn_gris.pack(side="left", padx=20, pady=10)
        btn_inverser.pack(side="left", padx=20, pady=10)
        btn_lisasage_con.pack(side="left", padx=20, pady=10)
        btn_filtrage_median.pack(side="left", padx=20, pady=10)
        btn_filtrage_lineaire.pack(side="left", padx=20, pady=10)
        btn_binariser.pack(side="left", padx=20, pady=10)
        btn_quitter.pack(side="right", padx=20, pady=10)

    def ouvrir_image(self):
        fichier = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.jpeg")])
        if not fichier:
            return
        self.image_originale = Image.open(fichier)
        self.image_result = self.image_originale
        self.afficher_image(self.image_originale)
        self.chemin_original = fichier

    def en_gris(self):
        if not self.image_originale:
            messagebox.showerror("Erreur", "Aucune image chargée")
            return
        self.image_gris = convertir_rgb_en_gris(self.image_originale)
        self.image_result = self.image_gris
        self.afficher_image(self.image_gris)
    
    def inverser(self):
        if not self.image_gris:
            messagebox.showerror("Erreur", "Convertis d'abord en niveaux de gris")
            return
        self.image_inverse = inverser_niveaux_de_gris(self.image_gris)
        self.image_result = self.image_inverse
        self.afficher_image(self.image_inverse)
        
    def sauvegarder_image(self):
        sauvegarder_image(self.image_result, self.chemin_original, "result")
        messagebox.showinfo("Succès", "Image inversée sauvegardée dans le dossier result/")
    
    def afficher_image(self, img):
        img_apercu = img.resize((650, 650))
        img_tk = ImageTk.PhotoImage(img_apercu)
        self.canvas.config(image=img_tk)
        self.canvas.image = img_tk
    
    def lissage_conservateur(self):
        if not self.image_gris:
            messagebox.showerror("Erreur", "Convertis d'abord en niveaux de gris")
            return
        self.image_lisse_cons = lissage_conservateur(self.image_gris)
        self.image_result = self.image_lisse_cons
        self.afficher_image(self.image_lisse_cons)
    
    def filtrage_median(self):
        if not self.image_gris:
            messagebox.showerror("Erreur", "Convertis d'abord en niveaux de gris")
            return
        self.image_filtre_median = filtrage_median(self.image_gris)
        self.image_result = self.image_filtre_median
        self.afficher_image(self.image_filtre_median)
    
    def conolution(self):
        if not self.image_gris:
            messagebox.showerror("Erreur", "Convertis d'abord en niveaux de gris")
            return
        filtre_moyenne = [
            [1/9, 1/9, 1/9],
            [1/9, 1/9, 1/9],
            [1/9, 1/9, 1/9]
        ]
        filtre_gaussien = [
            [1/16, 2/16, 1/16],
            [2/16, 4/16, 2/16],
            [1/16, 2/16, 1/16]
        ]

        self.image_convolution = filtrage_lineaire(self.image_gris, filtre_gaussien)
        self.image_result = self.image_convolution
        self.afficher_image(self.image_convolution)

    def binariser(self):
        if not self.image_gris:
            messagebox.showerror("Erreur", "Convertis d'abord en niveaux de gris")
            return
        self.image_binarise = binarisation_par_seuil(self.image_result)
        self.image_result = self.image_binarise
        self.afficher_image(self.image_binarise)
    
    def quitter(self):
        self.root.quit()
