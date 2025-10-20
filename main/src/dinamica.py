import tkinter as tk
from tkinter import filedialog
from functools import lru_cache

def roPD(input_file=None, output_file=None):
    """
    Programacion Dinamica para el problema del riego optimo.
    Recibe un archivo con formato:
    n
    ts0,tr0,p0
    ts1,tr1,p1
    ...
    Devuelve (orden optimo, costo minimo).
    """
    # Selección de archivo si no se pasa argumento
    if input_file is None:
        root = tk.Tk()
        root.withdraw()
        print("Seleccione el archivo de entrada (.txt)")
        input_file = filedialog.askopenfilename(
            title="Seleccionar archivo de entrada",
            filetypes=[("Archivos de texto", "*.txt")]
        )
        if not input_file:
            print("No se selecciono archivo. Saliendo...")
            return None, None

    # Lectura de datos
    with open(input_file, "r") as f:
        lineas = f.read().strip().split("\n")
        n = int(lineas[0])
        finca = [tuple(map(int, linea.split(","))) for linea in lineas[1:]]

    ts = [t[0] for t in finca]
    tr = [t[1] for t in finca]
    p  = [t[2] for t in finca]

    # Memoización con máscara de bits
    @lru_cache(maxsize=None)
    def dp(mask, tiempo_actual):
        """
        Retorna (costo minimo, orden optimo) para el conjunto 'mask' de tablones ya regados.
        """
        if mask == (1 << n) - 1:
            return 0, []  # todos regados

        mejor_costo = float("inf")
        mejor_orden = []

        for i in range(n):
            if not (mask & (1 << i)):  # si el tablón i aun no se ha regado
                nuevo_tiempo = tiempo_actual + tr[i]
                penalizacion = max(0, nuevo_tiempo - ts[i])
                costo = p[i] * penalizacion

                subcosto, suborden = dp(mask | (1 << i), nuevo_tiempo)
                total = costo + subcosto

                if total < mejor_costo:
                    mejor_costo = total
                    mejor_orden = [i] + suborden

        return mejor_costo, mejor_orden

    # Ejecutar DP desde estado inicial
    costo_total, mejor_orden = dp(0, 0)

    # Selección del archivo de salida si no se pasa
    if output_file is None:
        print("Seleccione dónde guardar el archivo de salida:")
        output_file = filedialog.asksaveasfilename(
            title="Guardar resultado",
            defaultextension=".txt",
            filetypes=[("Archivos de texto", "*.txt")]
        )
        if not output_file:
            print("No se seleccionó archivo de salida. Mostrando resultado en consola.")
            print("Costo total:", costo_total)
            print("Orden:", mejor_orden)
            return mejor_orden, costo_total

    # Guardar salida
    with open(output_file, "w") as f:
        f.write(f"{costo_total}\n")
        for idx in mejor_orden:
            f.write(f"{idx}\n")

    return mejor_orden, costo_total

# Si se ejecuta directamente el archivo:
if __name__ == "__main__":
    orden, costo = roPD()
    if orden is not None:
        print(f"\nOrden óptimo: {orden}")
        print(f"Costo total: {costo}")
