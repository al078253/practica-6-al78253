import tkinter as tk
from tkinter import ttk, scrolledtext
from tramos import agregar_tramo, calcular_tramos

root = tk.Tk()
root.title("Diseño de Carretera")
root.geometry("1000x700")
root.configure(bg="#e6f2ff")

# [Agregar aquí frame1, frame2, frame3 con los widgets como en tu código original]
# Botones:
# tk.Button(frame1, text="Agregar tramo", command=lambda: agregar_tramo(...))
# tk.Button(root, text="Calcular costos y riesgos", command=lambda: calcular_tramos(reporte_texto))

root.mainloop()
