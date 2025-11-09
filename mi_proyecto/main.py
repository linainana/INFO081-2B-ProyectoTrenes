import tkinter as tk
from ui import ventana

def main():
    try:
        root=tk.Tk()
        ventana.Ventana_principal(root)
        root.mainloop()
    except Exception as i:
        print(f"Error al iniciar la interfaz: {i}")

if __name__ == "__main__":
    main()
