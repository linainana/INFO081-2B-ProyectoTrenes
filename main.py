import tkinter as tk
import mi_proyecto.ui.ventana as ui

def main():
    try:
        ui
    except Exception as i:
        print(f"Error al iniciar la interfaz: {i}")



if __name__ == "__main__":
    main()
