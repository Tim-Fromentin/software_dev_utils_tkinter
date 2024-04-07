import tkinter as tk
from tkinter import *
from menu_option import menu_option_frame
from home_content import home_content
from mention_content import mention_content
from compressor_content import compressor_content
from db_generator_content import db_generator_content


win = tk.Tk()
win.geometry("800x500")
win.title("Utils")
win.configure(bg="white")
win.iconbitmap("./ressource/img/favicon.ico")

main = Frame(win, bg="white")
main.pack(fill=tk.BOTH, expand=True)

home_frame_widget = Frame(main, bg="white", padx=50)
home_content(home_frame_widget)
mention_frame_widget = Frame(main, bg="white")
mention_content(mention_frame_widget)
compressor_frame_widget = Frame(main, bg="white")
compressor_content(compressor_frame_widget)
db_generator_frame_widget = Frame(main, bg="white")
db_generator_content(db_generator_frame_widget)





def home_frame_action():
    mention_frame_widget.pack_forget()
    compressor_frame_widget.pack_forget()
    db_generator_frame_widget.pack_forget()
    home_frame_widget.pack(fill=tk.BOTH, expand=True)
    

def mention_frame_action():
    home_frame_widget.pack_forget()
    compressor_frame_widget.pack_forget()
    db_generator_frame_widget.pack_forget()
    mention_frame_widget.pack(fill=tk.BOTH, expand=True)

def compressor_frame_action():
    home_frame_widget.pack_forget()
    mention_frame_widget.pack_forget()
    db_generator_frame_widget.pack_forget()
    compressor_frame_widget.pack(fill=tk.BOTH, expand=True)

def db_generator_frame_action():
    home_frame_widget.pack_forget()
    mention_frame_widget.pack_forget()
    compressor_frame_widget.pack_forget()
    db_generator_frame_widget.pack(fill=BOTH, expand=True)


menu_option_frame(main, home_frame_action, mention_frame_action, compressor_frame_action, db_generator_frame_action)
home_frame_widget.pack()
win.mainloop()
