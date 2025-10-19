import os 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from main.src.bruta import roB

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

FILES = [
    "entrada_juguete.txt",
    "entrada_pequena.txt",
    "entrada_mediana.txt",
]
def test_archivos():
    for i in FILES:
        ruta = os.path.join(DATA_DIR, i)
        assert os.path.exists(ruta), f"No se encontró el archivo {i}"
def test_roB_funciona_con_FILES(tmp_path):
    for i in FILES:
        input = os.path.join(DATA_DIR, i)
        output = tmp_path / f"salida_{i}"
        orden, costo = roB(input, output)
        print(f"\nArchivo: {i} | Costo total: {costo} | Primeros índices: {orden[:5]}")

        assert isinstance(orden, tuple), f"{i}: la salida no es una tupla"
        assert isinstance(costo, float), f"{i}: el costo no es un float"
        assert len(orden) > 0, f"{i}: la lista de orden está vacía"
        assert output.exists(), f"{i}: no se creó el archivo de salida"

        contenido = output.read_text().strip().split("\n")
        costo_archivo = float(contenido[0])
        orden_archivo = list(map(int, contenido[1:]))

        assert costo == costo_archivo, f"{i}: el costo no coincide con el del archivo"
        assert set(orden_archivo) == set(range(len(orden_archivo))), f"{i}: el orden tiene repetidos o faltantes"
        