import tkinter as tk
from tkinter import filedialog
import heapq

def roD(input_file=None, output_file=None):
    if input_file is None:
        root = tk.Tk()
        root.withdraw()  
        print("Seleccione el archivo de entrada (.txt)")
        input_file = filedialog.askopenfilename(
            title="Seleccionar archivo de entrada",
            filetypes=[("Archivos de texto", "*.txt")]
        )

        if not input_file:
            print("No se seleccionó ningún archivo de entrada. Saliendo...")
            return None, None
        

    with open(input_file, "r") as f:
        lineas = f.read().strip().split("\n")
        n = int(lineas[0])
        finca = []
        for linea in lineas[1:]:
            ts, tr, p = map(int, linea.split(","))
            finca.append((ts, tr, p))


    heap = []
    for i in range(n):
        ts, tr, p = finca[i]
        heapq.heappush(heap, (ts, tr, p, i))

    tiempo_actual = 0
    costo_total = 0
    mejor_orden = []

    while heap:
        ts, tr, p, idx = heapq.heappop(heap)
        penalizacion = max(0, (tiempo_actual + tr) - ts)
        costo_total += p * penalizacion
        tiempo_actual += tr
        mejor_orden.append(idx)


    if output_file is None:
        print("Seleccione la ubicación para guardar el archivo de salida:")
        output_file = filedialog.asksaveasfilename(
            title="Guardar resultado",
            defaultextension=".txt",
            filetypes=[("Archivos de texto", "*.txt")]
        )

        if not output_file:
            print("Se debe seleccionar un archivo de salida. Saliendo...")
            return mejor_orden, costo_total

    with open(output_file, "w") as f:
        f.write(f"{costo_total}\n")
        for i in mejor_orden:
            f.write(f"{i}\n")

    return mejor_orden, costo_total