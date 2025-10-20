import tkinter as tk
from tkinter import filedialog 
import itertools

def roB(input_file=None, output_file=None):
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


    mejor_costo = float('inf')
    mejor_orden = []

    for perm in itertools.permutations(range(n)):
        tiempo_actual = 0
        costo_total = 0
        for i in perm:
            ts, tr, p = finca[i]
            penalizacion = max(0, (tiempo_actual + tr) - ts)
            costo_total += p * penalizacion
            tiempo_actual += tr
        if costo_total < mejor_costo:
            mejor_costo = costo_total
            mejor_orden = perm


    if output_file is None:
        print("Seleccione la ubicación para guardar el archivo de salida:")
        output_file = filedialog.asksaveasfilename(
            title="Guardar resultado",
            defaultextension=".txt",
            filetypes=[("Archivos de texto", "*.txt")]
        )

        if not output_file:
            print("Se debe seleccionar un archivo de salida. Saliendo...")
            return mejor_orden, mejor_costo

    with open(output_file, "w") as f:
        f.write(f"{mejor_costo}\n")
        for i in mejor_orden:
            f.write(f"{i}\n")

    print(f"\n Archivo guardado en: {output_file}")
    print(f"Orden de riego: {mejor_orden}")

    return mejor_orden, float(mejor_costo)
