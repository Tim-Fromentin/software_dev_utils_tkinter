import tkinter as tk
from tkinter import Button, Label, Entry
class MenuButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            relief=tk.FLAT,
            bd=0, 
            padx=20, 
            pady=10, 
            bg="white",
            fg="#191919"
        )
class BtnPrimary(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            relief=tk.FLAT,
            bd=0, 
            padx=20, 
            pady=10, 
            bg="#48BF84",
            fg="white"
        )
class Title(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            fg="#191919", bg="white", font=("Georgia", 25), padx=50
        )
class TitleInput(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            fg="#191919", bg="white", padx=50
        )
class Paragraph(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            padx=10, pady=10, wraplength=500, bg="white", fg="#191919"
        )
class InputPrimary(tk.Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            bg="#F7F7F7", fg="#191919"
        )

#FFFFFF
#0496FF
#9DE476
#191919
#E5625E