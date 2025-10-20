from src.voraz import roV
from src.bruta import roFB
from src.dinamica import roPD

if __name__ == "__main__":
    print("Elija el método para resolver el problema:")
    print("1. Algoritmo Bruto")
    print("2. Algoritmo Voraz")
    print("3. Algoritmo Dinámico")
    eleccion = input("Ingrese: ")
    if eleccion == "1":
        roFB()
    elif eleccion == "2":
        roV()
    elif eleccion == "3":
        roPD()
    else:
        print("Opción no válida. Saliendo...")

