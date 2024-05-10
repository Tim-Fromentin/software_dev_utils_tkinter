import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os


def compressor_action(image_name_label):
    global original_images, image_names
    image_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.jpg; *.jpeg; *.png; *.gif")])
    original_images = []  # Initialisation de la liste des images sélectionnées
    image_names = []  # Initialisation de la liste des noms de fichiers
    if image_paths:
        for image_path in image_paths:
            image_name = os.path.basename(image_path)  # Obtenir le nom de fichier à partir du chemin complet
            original_image = Image.open(image_path)  # Charger l'image avec PIL
            original_images.append(original_image)  # Ajouter l'image à la liste des images sélectionnées
            image_names.append(image_name)  # Ajouter le nom de fichier à la liste des noms de fichiers
        image_name_label.config(text="Selected Images: " + ', '.join(image_names))  # Mettre à jour le libellé avec les noms des images sélectionnées




def process_action(choice):
    global original_images, image_names
    if choice == "yes":
        for image_name, original_image in zip(image_names, original_images):
            # Créer une copie de l'image originale
            compressed_image = original_image.copy()
            # Effacer les données de l'image
            compressed_image.putdata([])
            # Sauvegarder l'image modifiée
            compressed_image.save(f'image_result/{image_name}_compress.webp')
        print("Data has been deleted.")
    else:
        print("Data will not be deleted.")