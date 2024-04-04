import tkinter as tk
from tkinter import * 
from menu_option import menu_option_frame
from home_frame_action import home_frame_action


win = tk.Tk()
win.geometry("800x500")
win.title("Utils")
win.configure(bg="white")
win.iconbitmap("./ressource/img/favicon.ico")



main = Frame(win, bg="white")
main.pack(fill=tk.BOTH, expand=True)

home_frame_widget = Frame(main, bg="red")
def home_frame_action():
    home_frame_widget.pack(fill=tk.BOTH, expand=True)
    l = Label(home_frame_widget,text="Home", fg="black", bg="white",font=("Lato", 25), justify=RIGHT).pack()


    
def mention_frame_action():
    print("g")




menu_option_frame(main,home_frame_action, mention_frame_action)

win.mainloop()
