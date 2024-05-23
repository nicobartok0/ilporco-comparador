import tkinter as Tk
from tkinter import *
from tkinter import ttk

# Se genera el elemento base de tkinter
root = Tk()
root.geometry("800x450")
root.title('Comparador Il Porco  0.0.1')
# Creamos un frame dentro de la ventana
frame = ttk.Frame(root, padding=10)
frame.grid()


# Activamos el loop principal 
if __name__ == '__main__':
    root.mainloop()


