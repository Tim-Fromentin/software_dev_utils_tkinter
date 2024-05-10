# mention_content.py
import tkinter as tk
from tkinter import * 
from tkinter import filedialog
from mention_frame.mention_action import mention_action_create_doc, file_path, file_name, mention_add_new_mention, mention_action_load_doc
from style import Title, BtnPrimary, TitleInput

def mention_content(mention_frame_widget):
    global mention_label_name_doc, mention_btn_create_doc, mention_title, mention_input_name_doc, mention_label_title, mention_label_position, mention_position, mention_label_type, mention_type, mention_label_source, mention_source, mention_btn_add_mention, file_path, file_name  # Ajouter file_path dans la liste des variables globales
    
    # Création des widgets
    mention_label = Title(mention_frame_widget, text="Mention")
    test = Label(mention_frame_widget, text=f"ff : {file_name}").pack()
    mention_label_name_doc = TitleInput(mention_frame_widget, text="Name of doc", fg="black",bg="white", font=("Lato", 15), justify=RIGHT)
    mention_input_name_doc = Entry(mention_frame_widget)
    mention_btn_create_doc = BtnPrimary(mention_frame_widget, text="create a new mention docs", command=lambda: mention_action_create_doc(mention_input_name_doc, mention_label_name_doc, mention_btn_create_doc, mention_title, mention_label_title, mention_label_position, mention_position, mention_label_type, mention_type, mention_label_source, mention_source, mention_btn_add_mention))

    mention_btn_load_doc = BtnPrimary(mention_frame_widget, text="load mention docs", command=lambda: mention_action_load_doc(mention_input_name_doc, mention_label_name_doc, mention_btn_load_doc, mention_title, mention_label_title, mention_label_position, mention_position, mention_label_type, mention_type, mention_label_source, mention_source, mention_btn_add_mention))
    
    mention_label_title = TitleInput(mention_frame_widget, text="Title mention")
    mention_title = Entry(mention_frame_widget)
    mention_label_position = TitleInput(mention_frame_widget, text="Position of content ex : header logo")
    mention_position = Entry(mention_frame_widget)
    mention_label_type = TitleInput(mention_frame_widget, text="Type of content : image, video..")
    mention_type = Entry(mention_frame_widget)
    mention_label_source = TitleInput(mention_frame_widget, text="Source of content ex : google.com")
    mention_source = Entry(mention_frame_widget)
    mention_btn_add_mention = BtnPrimary(mention_frame_widget, text="Add mention", command=lambda: mention_add_new_mention(mention_title, mention_position, mention_type, mention_source))

    # Placement des widgets avec pack()
    mention_label.pack(pady=15)
    mention_label_name_doc.pack(pady=15)
    mention_input_name_doc.pack(pady=15)
    mention_btn_create_doc.pack(pady=15)
    mention_btn_load_doc.pack()
    mention_label_title.pack()
    mention_title.pack()
    mention_label_position.pack()
    mention_position.pack()
    mention_label_type.pack()
    mention_type.pack()
    mention_label_source.pack()
    mention_source.pack()
    mention_btn_add_mention.pack()

