import tkinter as tk
from tkinter import *
from menu_option import menu_option_frame
from home_content import home_content
from mention_content import mention_content

win = tk.Tk()
win.geometry("800x500")
win.title("Utils")
win.configure(bg="white")
win.iconbitmap("./ressource/img/favicon.ico")

main = Frame(win, bg="white")
main.pack(fill=tk.BOTH, expand=True)

home_frame_widget = Frame(main, bg="white")
home_content(home_frame_widget)
mention_frame_widget = Frame(main, bg="white")
mention_content(mention_frame_widget)





def home_frame_action():
    mention_frame_widget.pack_forget()
    home_frame_widget.pack(fill=tk.BOTH, expand=True)
    

def mention_frame_action():
    home_frame_widget.pack_forget()
    mention_frame_widget.pack(fill=tk.BOTH, expand=True)

menu_option_frame(main, home_frame_action, mention_frame_action)

win.mainloop()
