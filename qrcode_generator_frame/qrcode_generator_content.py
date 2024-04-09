import tkinter as tk
from tkinter import *
from style import Title, BtnPrimary, TitleInput, InputPrimary

def qrcode_generator_content(qrcode_generator_frame_widget):
    qrg_title = Title(qrcode_generator_frame_widget, text="Qr code generator").pack(pady=15)
    qrg_label_link = TitleInput(qrcode_generator_frame_widget, text="Link").pack()
    qrg_input_link = InputPrimary(qrcode_generator_frame_widget).pack()
    qrg_btn_create = BtnPrimary(qrcode_generator_frame_widget, text="Create qr code")