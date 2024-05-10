# db_generator_action.py 
import tkinter as tk
from tkinter import filedialog
from tkinter import *
# NOTE finish

def db_generator_action(dbg_input_servername, dbg_input_name, dbg_input_password):
    name = dbg_input_name.get()
    servername = dbg_input_servername.get()
    password = dbg_input_password.get()
    file_path = filedialog.asksaveasfilename(defaultextension=".html",filetypes=[("PHP", "*.php")], title="create a new db doc", initialfile=f"db.php")
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write('<?php \n')
            file.write(f'$servername = "{servername}"; \n')
            file.write(f'$username = "{name}"; \n')
            file.write(f'$password = "{password}"; \n')
            file.write('$conn = new mysqli($servername, $username, $password);\n')
            file.write('if ($conn->connect_error) { \n')
            file.write('die("Connection failed: " . $conn->connect_error); \n')
            file.write('} \n')
            file.write('echo "Connected successfully"; \n')
            file.write('?>')