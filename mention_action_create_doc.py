# mention_action_create_doc.py
import tkinter as tk
from tkinter import filedialog

def mention_action_create_doc(mention_input_name_doc, mention_label_name_doc, mention_btn_create_doc, mention_title, mention_label_title, mention_label_position, mention_position, mention_label_type, mention_type, mention_label_source, mention_source, mention_btn_add_mention):
    title = mention_input_name_doc.get()
    file_path = filedialog.asksaveasfilename(defaultextension=".html",filetypes=[("HTML", "*.html")], title="create a new mention docs", initialfile=f"{title}.html")
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("Mention for {title} \n")
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
    mention_btn_add_mention.pack
