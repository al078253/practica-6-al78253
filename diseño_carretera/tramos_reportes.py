import tkinter as tk
from tkinter import messagebox
from materiales import calcular_materiales
from costos import calcular_costos
from riesgos import riesgos_geotecnicos, calcular_terraceria, calcular_drenaje

tramos = []

def agregar_tramo(entry_largo, entry_ancho, entry_espesor, var_pavimento, var_suelo, tree_tramos):
    try:
        largo = float(entry_largo.get())
        ancho = float(entry_ancho.get())
        espesor = float(entry_espesor.get())
        tipo_pav = var_pavimento.get()
        tipo_suelo = var_suelo.get()
        tramo = {"largo": largo, "ancho": ancho, "espesor": espesor, "tipo_pav": tipo_pav, "tipo_suelo": tipo_suelo}
        tramos.append(tramo)
        tree_tramos.insert('', 'end', values=(largo, ancho, espesor, tipo_pav, tipo_suelo))
        entry_largo.delete(0, tk.END)
        entry_ancho.delete(0, tk.END)
        entry_espesor.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"Valores inválidos: {e}")

def calcular_tramos(reporte_texto):
    if not tramos:
        messagebox.showwarning("Atención", "No hay tramos para calcular")
        return

    reporte_texto.delete(1.0, tk.END)
    total_general = 0

    for i, tramo in enumerate(tramos):
        v, cement, asf, grav, acero = calcular_materiales(tramo["largo"], tramo["ancho"], tramo["espesor"], tramo["tipo_pav"])
        costos = calcular_costos(cement, asf, grav, acero, v)
        corte, rell = calcular_terraceria(v, tramo["tipo_suelo"])
        dren = calcular_drenaje(tramo["largo"], tramo["ancho"])
        probs = riesgos_geotecnicos(tramo["tipo_suelo"], cement, asf, grav, acero)

        total_tramo = costos[-1]
        total_general += total_tramo

        reporte_texto.insert(tk.END, f"--- Tramo {i+1} ---\n")
        reporte_texto.insert(tk.END, f"Largo: {tramo['largo']} m, Ancho: {tramo['ancho']} m\n")
        reporte_texto.insert(tk.END, f"Espesor: {tramo['espesor']} cm, Pavimento: {tramo['tipo_pav']}, Suelo: {tramo['tipo_suelo']}\n")
        reporte_texto.insert(tk.END, f"Volumen pavimento: {v:.2f} m³\n")
        reporte_texto.insert(tk.END, f"Cemento: {cement:.2f} t, Asfalto: {asf:.2f} t, Grava: {grav:.2f} t, Acero: {acero:.2f} kg\n")
        reporte_texto.insert(tk.END, f"Costos: Cemento ${costos[0]:.2f}, Asfalto ${costos[1]:.2f}, Grava ${costos[2]:.2f}, Acero ${costos[3]:.2f}, Mano de Obra ${costos[4]:.2f}, Maquinaria ${costos[5]:.2f}\n")
        reporte_texto.insert(tk.END, f"Total Tramo: ${total_tramo:.2f}\n")
        reporte_texto.insert(tk.END, f"Corte: {corte:.2f} m³, Relleno: {rell:.2f} m³\n")
        reporte_texto.insert(tk.END, f"Drenaje estimado: {dren:.2f} m\n")
        reporte_texto.insert(tk.END, "Problemas / Riesgos geotécnicos:\n")
        for p in probs:
            reporte_texto.insert(tk.END, f"  • {p}\n")
        reporte_texto.insert(tk.END, "\n")

    reporte_texto.insert(tk.END, f"=== COSTO TOTAL PROYECTO: ${total_general:.2f} ===\n")
