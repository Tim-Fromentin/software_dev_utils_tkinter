import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


def compressor_action(image_label,choice_del_data):
    global original_image
    # Demander à l'utilisateur de sélectionner une image
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg; *.jpeg; *.png; *.gif")])
    
    # Vérifier si l'utilisateur a sélectionné une image
    if image_path:
        # Charger l'image avec PIL
        original_image = Image.open(image_path)
        
        # Convertir l'image PIL en format compatible avec Tkinter
        tk_image = ImageTk.PhotoImage(original_image)
        
        # Mettre à jour l'étiquette de l'image avec la nouvelle image
        image_label.config(image=tk_image)
        image_label.image = tk_image  # Conserver une référence à l'image pour éviter qu'elle ne soit effacée par le garbage collector


import os

def process_action(choice):
    global original_image
    if choice == "yes":
        # Supprimer les données de l'image
        original_image.putdata([])

        # Créer le répertoire s'il n'existe pas
        os.makedirs('image_result', exist_ok=True)

        # Sauvegarder l'image modifiée
        original_image.save('image_result/newfile.webp')
        print("Data has been deleted.")
    else:
        print("Data will not be deleted.")
