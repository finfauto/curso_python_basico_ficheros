import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog="contador_fichero",
        description="Programa para hacer recuentos en el fichero"
    )
    parser.add_argument(
        "--file", required=True, help="Fichero que vamos a usar"
    )
    parser.add_argument(
        "--contar_palabras", type=bool, default=True, help="Si activa esta función, devuelve el número de palabras"
    )
    parser.add_argument(
        "--contar_lineas", type=bool, default=True, help="Si activa esta función, devuelve el número de líneas"
    )

    return parser.parse_args()


def contar_palabras(fichero):
    with open(fichero, 'r') as f:
        caracteres_fichero = f.read()
        palabras = caracteres_fichero.split()
    return len(palabras)


def contar_lineas(fichero):
    with open(fichero, 'r') as f:
        lineas = f.readlines()
    return len(lineas)


if __name__ == "__main__":
    args = parse_args()
    if args.contar_palabras:
        print(f"El número de palabras es: {contar_palabras(args.file)}")
    if args.contar_lineas:
        print(f"El número de líneas es: {contar_lineas(args.file)}")
