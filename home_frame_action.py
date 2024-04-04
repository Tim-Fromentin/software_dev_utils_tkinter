import tkinter as tk
from tkinter import * 

def home_frame_action(main):
    home_frame_widget = Frame(main, bg="green")
    home_frame_widget.pack(fill=tk.BOTH, expand=True)
    home_frame_widget.pack()
    l = Label(home_frame_widget,text="Home", fg="black", bg="white",font=("Lato", 25), justify=RIGHT).pack()
