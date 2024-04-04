import tkinter as tk
from tkinter import * 


def menu_option_frame(main,home_frame_action, mention_frame_action):
    menu_option = Frame(main, bg="#E4EAF8", width=150, padx=150)
    menu_option.pack(side="left", fill="y")
    btn_choice_home = Button(menu_option, text="Home", command=home_frame_action)
    btn_choice_home.pack()
    btn_choice_mention = Button(menu_option, text="Mention", command=mention_frame_action)
    btn_choice_mention.pack()

