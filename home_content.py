import tkinter as tk
from tkinter import * 

def home_content(home_frame_widget):
    home_label = Label(home_frame_widget, text="Home", fg="black", bg="white", font=("Lato", 25), justify=RIGHT)
    home_label.pack()
    home_txt = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde, placeat laudantium. Eligendi tempora pariatur cumque earum quis eos distinctio nostrum alias suscipit corrupti, voluptates ipsam? Perspiciatis accusamus numquam, earum corporis sequi quis. Beatae nihil quae, rerum, unde in provident quibusdam asperiores quia ducimus similique distinctio exercitationem reiciendis. Eaque, rerum repudiandae!ttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt"
    home_txt_label = Label(home_frame_widget, justify=CENTER, text=home_txt, padx=10, pady=10, wraplength=500)
    home_txt_label.pack()
    