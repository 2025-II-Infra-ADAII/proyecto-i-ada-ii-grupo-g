import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from main.src.dinamica import roD

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

FILES = [
    "entrada_juguete.txt",
    "entrada_pequena.txt",
    "entrada_mediana.txt",
    "entrada_grande.txt",
    "entrada_extragrande.txt",
]

def test_archivos():
    for i in FILES:
        ruta = os.path.join(DATA_DIR, i)
        assert os.path.exists(ruta), f"No se encontró el archivo {i}"

def test_roD_funciona_con_FILES(tmp_path):
    repeticiones = 3
    for i in FILES:
        input = os.path.join(DATA_DIR, i)
        output = tmp_path / f"salida_{i}"

        tiempos = []
        for _ in range(repeticiones):
            inicio = time.time()
            orden, costo = roD(input, output)
            fin = time.time()
            tiempos.append(fin - inicio)

        tiempo_promedio = sum(tiempos) / repeticiones
        print(f"\nArchivo: {i} | Costo total: {costo} | Tiempo promedio: {tiempo_promedio:.4f}s | Primeros índices: {orden[:5]}")

        assert isinstance(orden, list), f"{i}: la salida no es una lista"
        assert isinstance(costo, int), f"{i}: el costo no es un int"
        assert len(orden) > 0, f"{i}: la lista de orden está vacía"
        assert output.exists(), f"{i}: no se creó el archivo de salida"

        contenido = output.read_text().strip().split("\n")
        costo_archivo = int(contenido[0])
        orden_archivo = list(map(int, contenido[1:]))

        assert costo == costo_archivo, f"{i}: el costo no coincide con el del archivo"
        assert set(orden_archivo) == set(range(len(orden_archivo))), f"{i}: el orden tiene repetidos o faltantes"
