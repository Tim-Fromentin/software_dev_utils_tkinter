# mention_widgets.py
from tkinter import Label, Entry, Button

def create_mention_widgets(mention_frame_widget):
    mention_label_title = Label(mention_frame_widget, text="Title mention")
    mention_title = Entry(mention_frame_widget)
    mention_label_position = Label(mention_frame_widget, text="Position of content ex : header logo")
    mention_position = Entry(mention_frame_widget)
    mention_label_type = Label(mention_frame_widget, text="Type of content : image, video..")
    mention_type = Entry(mention_frame_widget)
    mention_label_source = Label(mention_frame_widget, text="Source of content ex : google.com")
    mention_source = Entry(mention_frame_widget)
    mention_btn_add_mention = Button(mention_frame_widget, text="Add mention")

    return mention_label_title, mention_title, mention_label_position, mention_position, mention_label_type, mention_type, mention_label_source, mention_source, mention_btn_add_mention
