import tkinter as Tk
from tkinter import *
from tkinter import ttk
import tkinter.filedialog
from operador import Operador

# Se genera el elemento base de tkinter
root = Tk()
root.geometry("1200x450")
root.title('Comparador Il Porco  0.0.1')
# Creamos un frame dentro de la ventana
frame = ttk.Frame(root, padding=10)
frame.pack()

#Creamos el operador
operador = Operador()

#Creamos la matriz donde estarán todas las labels de precios
pricelabels = [[]]

# Funcionalidades

def cargar_datos():
    ruta = tkinter.filedialog.askopenfilename()
    index = ruta.split('/')
    nombre = index[-1]
    nombre = nombre[:-5]
    operador.crear_lector(nombre, ruta)
    operador.crear_articulos()
    print(operador.articulos)
    rowcount = 0
    
    for key in operador.articulos.keys():
        ttk.Label(master=frame_app, text=key).grid(row=2+rowcount, column=0)
        ttk.Label(master=frame_app, text=operador.articulos[key].nombre).grid(row=2+rowcount, column=1)
        colcount = 0
        if len(pricelabels) <= rowcount:
            pricelabels.append([])
        for precio in operador.articulos[key].precios.values():
            label = ttk.Label(master=frame_app, text=precio)
            pricelabels[rowcount].append(label)
            label.grid(row=2+rowcount, column=2+colcount)
            colcount += 1

        ttk.Label(master=frame_app, text=operador.articulos[key].costo).grid(row=2+rowcount, column=9)
        rowcount += 1
    print(f'{pricelabels}')

    # Añadir Scrollbar al mainframe
    scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Configurar canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

def buscar_precios():
    operador.articulos = operador.inicializar(frame_app)

def refresh_precios():
    rowcount = 0
    for key in operador.articulos.keys():
        colcount = 0
        for precio in operador.articulos[key].precios.values():
            print(f'{rowcount}:{colcount}')
            pricelabels[rowcount][colcount].config(text=precio)
            colcount += 1
        rowcount += 1
        



# --- CONFIGURACIÓN DE LA GUI PARA EL USO DE SCROLLBARS ---

# Crear un main frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Crear un canvas
canvas = Canvas(main_frame)
canvas.pack(side=LEFT, fill=BOTH, expand=1)



# Crear otro frame donde estarán los widgets
frame_app = Frame(canvas)
frame_app.bind('<<ArticleDone>>', lambda e: refresh_precios())

# Crear frame como ventana del canvas
canvas.create_window((0,0), window=frame_app, anchor="nw")

# --- FIN DE CONFIGURACIÓN DE LA GUI PARA EL USO DE SCROLLBARS ---

# GUI

# Botones de cargar datos y buscar precios
ttk.Button(master=frame_app, text='Cargar Datos', command=cargar_datos).grid(row=0, column=1, padx=10, pady=10)
ttk.Button(master=frame_app, text='Buscar Precios', command=buscar_precios).grid(row=0, column=7, padx=10, pady=10)

# Labels de cabecera de la tabla
ttk.Label(master=frame_app, text='Código').grid(row=1, column=0, padx=10, pady=10)
ttk.Label(master=frame_app, text='Nombre').grid(row=1, column=1, padx=100, pady=10)
ttk.Label(master=frame_app, text='Cagnoli').grid(row=1, column=2, padx=20, pady=10)
ttk.Label(master=frame_app, text='Los Calvos').grid(row=1, column=3, padx=20, pady=10)
ttk.Label(master=frame_app, text='Nahuel').grid(row=1, column=4, padx=20, pady=10)
ttk.Label(master=frame_app, text='Doina').grid(row=1, column=5, padx=20, pady=10)
ttk.Label(master=frame_app, text='Las Dinas').grid(row=1, column=6, padx=20, pady=10)
ttk.Label(master=frame_app, text='Cabañas Argentinas').grid(row=1, column=7, padx=20, pady=10)
ttk.Label(master=frame_app, text='Otras marcas').grid(row=1, column=8, padx=20, pady=10)
ttk.Label(master=frame_app, text='Il Porco').grid(row=1, column=9, padx=20, pady=10)

# Activamos el loop principal 
if __name__ == '__main__':
    root.mainloop()


