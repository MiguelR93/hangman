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
    # alea = random.randint(0,len(data))
    elegidaNato = origin[random.randint(0,len(data))]
    elegidaA = elegidaNato.replace("á",'a')
    elegidaE = elegidaA.replace('é','e')
    elegidaI = elegidaE.replace('í','i')
    elegidaO = elegidaE.replace('ó','o')
    elegida = elegidaO.replace('ú','u')
    # # aquí planeo guardar lo que el jugador va develando
    # descubierto = len(elegida)*"_"
    descubierto = {i:"_" for i in range(len(elegida))}
    print(f"esto es descubierto: {descubierto}")
    # print(alea)
    # # imprimir los espacios que ocupa la palabra y el mensaje de interacción con el usuario
    # input(f"""{descubierto}\n\nIngresa una letra: """)
    # # pedirle al usuario que ingrese una letra hasta que adivine


    # # temporalmente mostramos la palabra aleatoria
    palabra = {i:a for i,a in enumerate(elegida)}
    print(f"esto es palabra: {palabra}")

    # estado = palabra == descubierto

    # print(f"son iguales la elegida y la descubierta? {estado}")

    # # aquí empezamos a jugar
    while palabra != descubierto:
        for i in descubierto.values():
            print(i.upper(), end=" ")
        letra = input("""\n\nIngresa una letra: """)
        for i,a in palabra.items():
            # print(f"{i}:{a}")
            if letra == palabra[i]:
                # # si esto es verdad, debemos alterar a "descubierto"
                # print("sí")
                # # con esta línea sustituimos
                descubierto[i] = letra
    for i in descubierto.values():
            print(i.upper(), end="")
    print("")




if __name__ == "__main__":
    # # inicio
    run()