# mention_content.py
import tkinter as tk
from tkinter import * 
from tkinter import filedialog
from mention_action import mention_action_create_doc, file_path  # Importer file_path depuis mention_action_create_doc
from mention_action import mention_add_new_mention
from style import Title, BtnPrimary, TitleInput

def mention_content(mention_frame_widget):
    global mention_label_name_doc, mention_btn_create_doc, mention_title, mention_input_name_doc, mention_label_title, mention_label_position, mention_position, mention_label_type, mention_type, mention_label_source, mention_source, mention_btn_add_mention, file_path  # Ajouter file_path dans la liste des variables globales
    mention_label = Title(mention_frame_widget, text="Mention").pack(pady=15)
    mention_label_name_doc = TitleInput(mention_frame_widget, text="Name of doc", fg="black",bg="white", font=("Lato", 15), justify=RIGHT).pack()
    mention_input_name_doc = Entry(mention_frame_widget).pack(pady=15)
    mention_btn_create_doc = BtnPrimary(mention_frame_widget, text="create a new mention docs", command=lambda: mention_action_create_doc(mention_input_name_doc, mention_label_name_doc, mention_btn_create_doc, mention_title, mention_label_title, mention_label_position, mention_position, mention_label_type, mention_type, mention_label_source, mention_source, mention_btn_add_mention)).pack(pady=15)

    mention_label_title = TitleInput(mention_frame_widget, text="Title mention")
    mention_title = Entry(mention_frame_widget)
    mention_label_position = TitleInput(mention_frame_widget, text="Position of content ex : header logo")
    mention_position = Entry(mention_frame_widget)
    mention_label_type = TitleInput(mention_frame_widget, text="Type of content : image, video..")
    mention_type = Entry(mention_frame_widget)
    mention_label_source = TitleInput(mention_frame_widget, text="Source of content ex : google.com")
    mention_source = Entry(mention_frame_widget)
    mention_btn_add_mention = BtnPrimary(mention_frame_widget, text="Add mention", command=lambda: mention_add_new_mention(mention_title, mention_position, mention_type, mention_source))
