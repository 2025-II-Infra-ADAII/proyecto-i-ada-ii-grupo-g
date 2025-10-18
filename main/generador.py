import random

def generar_finca(n, nombre_archivo):
    with open(nombre_archivo, "w") as f:
        f.write(f"{n}\n")
        for _ in range(n):
            ts = random.randint(5, 50)    
            tr = random.randint(1, 10)  
            p = random.randint(1, 4)       
            f.write(f"{ts},{tr},{p}\n")
    print(f"Archivo generado: {nombre_archivo}")

if __name__ == "__main__":
    random.seed(42)
    tamaños = {
        "entrada_juguete.txt": 10,
        "entrada_pequena.txt": 100,
        "entrada_mediana.txt": 1000,
        "entrada_grande.txt": 10000,
        "entrada_extragrande.txt": 50000,
    }

    for nombre, n in tamaños.items():
        generar_finca(n, nombre)
