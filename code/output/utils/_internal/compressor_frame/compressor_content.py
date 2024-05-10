import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image
from compressor_frame.compressor_action import compressor_action, process_action
from style import Title, BtnPrimary, TitleInput


def compressor_content(compressor_frame_widget):
    compressor_label = Title(compressor_frame_widget, text="Compressor").pack()
    global image_name_label
    # Créer une étiquette pour l'image
    image_name_label = TitleInput(compressor_frame_widget, text="", font=("Helvetica", 12))
    image_name_label.pack(pady=10)
    
    # Variable pour stocker l'état de la case à cocher
    choice_del_data = tk.StringVar()
    
    choice_img = Button(compressor_frame_widget, text="Choice image", command=lambda: compressor_action(image_name_label))
    choice_img.pack()
    
    # Créer la case à cocher avec la variable choice_del_data
    choice_del_checkbox = Checkbutton(compressor_frame_widget, text="Delete data", variable=choice_del_data, onvalue="yes", offvalue="no")
    choice_del_checkbox.pack()
    
    btn_compress = BtnPrimary(compressor_frame_widget, text="Process", command=lambda: process_action(choice_del_data.get()))
    btn_compress.pack()