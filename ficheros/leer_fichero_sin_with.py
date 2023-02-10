if __name__ == "__main__":
    fichero = open("cualquier_fichero.txt", 'r')
    try:
        fichero.read()
    finally:
        fichero.close()
