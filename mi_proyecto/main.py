import tkinter as tk
import json
import os
from ui.ventana_principal import Ventana_principal


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_DIR = os.path.join(BASE_DIR, "config")

with open(os.path.join(CONFIG_DIR, "ventana.json"), "r", encoding="utf-8") as f:
    ventana = json.load(f)

with open(os.path.join(CONFIG_DIR, "colores.json"), "r", encoding="utf-8") as f:
    colores = json.load(f)

if __name__ == "__main__":
    root = tk.Tk()
    Ventana_principal(root, ventana, colores)
    root.mainloop()