import tkinter as tk
from tkinter import * 
from style import Title, Paragraph

def home_content(home_frame_widget):
    home_label = Title(home_frame_widget, text="Home")
    home_label.pack()
    home_txt = "Royalty-free software created by tim fromentin. Software designed to provide tools for web developers. It's not professional software, just a personal project."
    home_txt_label = Paragraph(home_frame_widget, text=home_txt)
    home_txt_label.pack()
    