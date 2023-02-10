import os

if __name__ == "__main__":
    ruta_fichero = os.path.join("data", "fichero.txt")
    with open(ruta_fichero, 'r') as fichero:
        texto = fichero.read()
        print(texto)
