import tkinter as tk
from tkinter import *
import qrcode

def qrcode_generator_action(qrg_input_link, qrg_input_title):
    link = qrg_input_link.get()
    title = qrg_input_title.get()
    qrcode_img = qrcode.make(link)
    type(qrcode_img)
    qrcode_img.save(f"qrcode_img/{title}.png")
    qrg_input_link.delete(0, END)
    qrg_input_title.delete(0, END)
