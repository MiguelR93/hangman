import random, os

def run():
    # # limpiando la pantalla
    os.system("clear")
    # # creando una lista que contendrá las palabras del documento "data.txt"
    data = []
    # # extrayendo las palabras de "data.txt"
    with open("./data.txt", "r", encoding="utf-8") as word:
        for i in word:
            width = len(i) - 1
            data.append(i[:width])
    # print(data)
    origin = {n:data[n] for n in range(len(data))}
    # print(origin)
    # # elegir una palabra aleatoriamente desde origin:
    # print(len(data))
    alea = random.randint(0,len(data))
    elegida = origin[alea]
    # print(alea)
    # # imprimir los espacios que ocupa la palabra y el mensaje de interacción con el usuario
    input(f"""{len(elegida)*"_ "}\n\nIngresa una letra: """)
    # # pedirle al usuario que ingrese una letra hasta que adivine    


if __name__ == "__main__":
    # # inicio
    run()