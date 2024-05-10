# import
import tkinter as tk
from tkinter import filedialog
from tkinter import * 

# window 
win = tk.Tk()
# window style
win.geometry("800x500")
win.title("Utils")
win.configure(bg="white")
win.iconbitmap("./ressource/img/favicon.ico")







# home frame
home_frame = tk.Frame(win, bg="white")
tk.Label(home_frame,text="Home", fg="black", bg="white",font=("Lato", 25), justify=CENTER).pack()
tk.Label(home_frame,text="lorem", fg="black", bg="white",font=("Lato", 16), justify=CENTER).pack()

def choice_mention():
    # Masquer les autres pages et afficher la page de la mention
    home_frame.pack_forget()
    mention_frame.pack(fill=tk.BOTH, expand=True)

def choice_home():
    # Masquer les autres pages et afficher la page d'accueil
    mention_frame.pack_forget()
    home_frame.pack(fill=tk.BOTH, expand=True)

# left nav
option_frame = tk.Frame(win, bd=1, bg="gray")
choice_home = tk.Button(option_frame, text="Home", font=("Lato"), fg="black", command=choice_home).place(x=20,y=20)
choice_mention = tk.Button(option_frame, text="Mentions", font=("Lato"), fg="black", command=choice_mention).place(x=20,y=60)

option_frame.pack(side=tk.LEFT, fill="y")
option_frame.pack_propagate(False)
option_frame.config(width=150)



# mention frame
mention_frame = tk.Frame(win, bg="white")
button_create = Button(mention_frame, text="Create document")
button_create.pack()
button_continue = Button(mention_frame, text="Continue document")
button_continue.pack()




# choice_home()
win.mainloop()
