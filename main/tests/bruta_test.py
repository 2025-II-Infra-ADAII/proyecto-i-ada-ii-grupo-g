import os
import sys
import time
import statistics

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from main.src.bruta import roFB

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

FILES = [
    "entrada_juguete.txt",       # 10 elementos
    #Usar pequeña en adelante, lleva demasiado tiempo
]

def test_archivos():
    for i in FILES:
        ruta = os.path.join(DATA_DIR, i)
        assert os.path.exists(ruta), f"No se encontró el archivo {i}"

def test_roB_funciona_con_FILES(tmp_path):
    REPETICIONES = 5

    for i in FILES:
        input_path = os.path.join(DATA_DIR, i)
        output_path = tmp_path / f"salida_{i}"

        tiempos = []

        for r in range(REPETICIONES):
            inicio = time.perf_counter()
            orden, costo = roFB(input_path, output_path)
            fin = time.perf_counter()
            tiempos.append(fin - inicio)

            assert isinstance(orden, tuple), f"{i}: la salida no es una tupla"
            assert isinstance(costo, float), f"{i}: el costo no es un float"
            assert len(orden) > 0, f"{i}: la lista de orden está vacía"
            assert output_path.exists(), f"{i}: no se creó el archivo de salida"

            contenido = output_path.read_text().strip().split("\n")
            costo_archivo = float(contenido[0])
            orden_archivo = list(map(int, contenido[1:]))

            assert costo == costo_archivo, f"{i}: el costo no coincide con el del archivo"
            assert set(orden_archivo) == set(range(len(orden_archivo))), f"{i}: el orden tiene repetidos o faltantes"

        print(f"\n=== Resultados para {i} ===")
        print(f"Repeticiones: {REPETICIONES}")
        print(f"Tiempos individuales: {[round(t, 4) for t in tiempos]}")
        print(f"Tiempo promedio: {statistics.mean(tiempos):.4f} s")
        print(f"Tiempo mínimo: {min(tiempos):.4f} s")
        print(f"Tiempo máximo: {max(tiempos):.4f} s")
        print("============================\n")
