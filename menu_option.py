import tkinter as tk
from tkinter import * 


def menu_option_frame(main,home_frame_action, mention_frame_action, compressor_frame_action, db_generator_action):
    menu_option = Frame(main, bg="#E4EAF8", padx=50)
    menu_option.pack(side="left", fill="y")
    btn_choice_home = Button(menu_option, text="Home", command=home_frame_action)
    btn_choice_home.pack()
    btn_choice_mention = Button(menu_option, text="Mention", command=mention_frame_action)
    btn_choice_mention.pack()
    btn_choice_compressor = Button(menu_option, text="Compress img", command=compressor_frame_action)
    btn_choice_compressor.pack()
    btn_choice_bd_generator = Button(menu_option, text="Db generator", command=db_generator_action)
    btn_choice_bd_generator.pack()

