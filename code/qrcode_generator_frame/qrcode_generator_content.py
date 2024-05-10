import tkinter as tk
from tkinter import *
from qrcode_generator_frame.qrcode_generator_action import qrcode_generator_action
from style import Title, BtnPrimary, TitleInput, InputPrimary

def qrcode_generator_content(qrcode_generator_frame_widget):
    global qrg_input_link, qrg_input_title
    qrg_title = Title(qrcode_generator_frame_widget, text="Qr code generator").pack(pady=15)
    qrg_label_title = TitleInput(qrcode_generator_frame_widget, text="Title file").pack()
    qrg_input_title = InputPrimary(qrcode_generator_frame_widget)
    qrg_input_title.pack()
    qrg_label_link = TitleInput(qrcode_generator_frame_widget, text="Link").pack()
    qrg_input_link = InputPrimary(qrcode_generator_frame_widget)
    qrg_input_link.pack()
    qrg_btn_create = BtnPrimary(qrcode_generator_frame_widget, text="Create qr code", command=lambda: qrcode_generator_action(qrg_input_link, qrg_input_title)).pack()