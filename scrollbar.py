from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Pruebas scrollbar')
root.geometry('500x400')

# Create a main frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create a canvas 
canvas = Canvas(main_frame)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add a Scrollbar to canvas
scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure the canvas 
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

# Create another frame inside Canvas
frame_app = Frame(canvas)

# Add new frame to a window in the canvas
canvas.create_window((0,0), window=frame_app, anchor="nw")

for thing in range(100):
    Button(frame_app, text=f'Botón {thing}').grid(row=thing, column=0, padx=10, pady=10)

root.mainloop()