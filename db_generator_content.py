# db_generator_content.py 
import tkinter as tk
from tkinter import *
from style import Title, BtnPrimary, TitleInput
from db_generator_action import db_generator_action

def db_generator_content(db_generator_frame_widget):
    dbg_title = Title(db_generator_frame_widget, text="DataBase generator").pack()
    dbg_label_servername = TitleInput(db_generator_frame_widget, text="Server name").pack()
    dbg_input_servername = Entry(db_generator_frame_widget)
    dbg_input_servername.pack(pady=15)
    dbg_label_name = TitleInput(db_generator_frame_widget, text="username").pack()
    dbg_input_name = Entry(db_generator_frame_widget)
    dbg_input_name.pack(pady=15)
    dbg_label_password = TitleInput(db_generator_frame_widget, text="Password").pack()
    dbg_input_password = Entry(db_generator_frame_widget)
    dbg_input_password.pack(pady=15)
    dbg_btn_create_doc = BtnPrimary(db_generator_frame_widget, text="create doc", command=lambda: db_generator_action(dbg_input_servername, dbg_input_name, dbg_input_password)).pack()