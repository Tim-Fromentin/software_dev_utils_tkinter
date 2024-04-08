import tkinter as tk
from tkinter import * 
from style import MenuButton

def menu_option_frame(main,home_frame_action, mention_frame_action, compressor_frame_action, db_generator_action):
    menu_option = Frame(main, bg="#4472CA", padx=50)
    menu_option.pack(side="left", fill="y")
    btn_choice_home = MenuButton(menu_option, text="Home", command=home_frame_action).pack(pady=(10, 0))
    btn_choice_mention = MenuButton(menu_option, text="Mention", command=mention_frame_action).pack(pady=(10, 0))
    btn_choice_compressor = MenuButton(menu_option, text="Compress img", command=compressor_frame_action).pack(pady=(10, 0))
    btn_choice_bd_generator = MenuButton(menu_option, text="Db generator", command=db_generator_action).pack(pady=(10, 0))

