import tkinter as tk
from tkinter import filedialog

def roV(input_file=None, output_file=None):
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


    tablones_con_clave = []
    for i, (ts, tr, p) in enumerate(finca):
        clave = p / tr
        tablones_con_clave.append((i, ts, tr, p, clave))
    tablones_ordenados = sorted(tablones_con_clave, key=lambda x: x[4], reverse=True)
    tiempo_actual = 0
    costo_total = 0
    for _, ts, tr, p, _ in tablones_ordenados:
        penalizacion = max(0, (tiempo_actual + tr) - ts)
        costo_total += p * penalizacion
        tiempo_actual += tr
    orden = [t[0] for t in tablones_ordenados]


    if output_file is None:
        print("Seleccione la ubicación para guardar el archivo de salida:")
        output_file = filedialog.asksaveasfilename(
            title="Guardar resultado",
            defaultextension=".txt",
            filetypes=[("Archivos de texto", "*.txt")]
        )

        if not output_file:
            print("Se debe seleccionar un archivo de salida. Saliendo...")
            return orden, costo_total

    with open(output_file, "w") as f:
        f.write(f"{costo_total}\n")
        for i in orden:
            f.write(f"{i}\n")

    print(f"\n Archivo guardado en: {output_file}")
    print(f"Orden de riego: {orden}")
    print(f"Costo total: {costo_total}")

    return orden, costo_total
