# mention_action_create_doc.py
import tkinter as tk
from tkinter import filedialog
from tkinter import *
# TODO create a action for loading old file


file_path = None  # Déclaration de la variable globale file_path initialisée à None
file_name = ""

def mention_action_create_doc(mention_input_name_doc, mention_label_name_doc, mention_btn_create_doc, mention_title, mention_label_title, mention_label_position, mention_position, mention_label_type, mention_type, mention_label_source, mention_source, mention_btn_add_mention):
    global file_path, file_name
    title = mention_input_name_doc.get()
    file_path = filedialog.asksaveasfilename(defaultextension=".html",filetypes=[("HTML", "*.html")], title="create a new mention docs", initialfile=f"{title}.html")
    if file_path:
        file_name = file_path.split("/")[-1]  # Extraire le nom du fichier à partir du chemin complet
        print("Fichier sélectionné :", file_name)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(f"Mention for {title}\n")
            file.write("Contenu : Ensemble des éléments constituants l’information présente sur le Site, notamment textes – images – vidéos.Liste des images non propriétaires :")
    mention_label_name_doc.pack_forget()
    mention_btn_create_doc.pack_forget()
    mention_input_name_doc.pack_forget()
    mention_label_title.pack()
    mention_title.pack()
    mention_label_position.pack()
    mention_position.pack()
    mention_label_type.pack()
    mention_type.pack()
    mention_label_source.pack()
    mention_source.pack()
    mention_btn_add_mention.pack()

def mention_action_load_doc(mention_input_name_doc, mention_label_name_doc, mention_btn_create_doc, mention_title, mention_label_title, mention_label_position, mention_position, mention_label_type, mention_type, mention_label_source, mention_source, mention_btn_add_mention):
    global file_path  # Utilisation de la variable globale file_path
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.html")])
    mention_label_name_doc.pack_forget()
    mention_btn_create_doc.pack_forget()
    mention_input_name_doc.pack_forget()
    mention_label_title.pack()
    mention_title.pack()
    mention_label_position.pack()
    mention_position.pack()
    mention_label_type.pack()
    mention_type.pack()
    mention_label_source.pack()
    mention_source.pack()
    mention_btn_add_mention.pack()




def mention_add_new_mention(mention_title, mention_position, mention_type, mention_source):
    global file_path  # Utilisation de la variable globale file_path
    title = mention_title.get()
    position = mention_position.get()
    content_type = mention_type.get()
    source = mention_source.get()
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f'<a href="{source}">{content_type} {position} ({title})</a>,\n')
    mention_title.delete(0, END)
    mention_position.delete(0, END)
    mention_type.delete(0, END)
    mention_source.delete(0, END)
