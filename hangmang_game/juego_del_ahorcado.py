import random, os

def run():
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
    # print(f"esto es elegidaA: {elegidaA}")
    elegidaE = elegidaA.replace('é','e')
    # print(f"esto es elegidaE: {elegidaE}")
    elegidaI = elegidaE.replace('í','i')
    # print(f"esto es elegidaI: {elegidaI}")
    elegidaO = elegidaI.replace('ó','o')
    # print(f"esto es elegidaO: {elegidaO}")
    elegidaU = elegidaO.replace('ú','u')
    # print(f"esto es elegidaU: {elegidaU}")
    elegida = elegidaU.upper()
    # print(f"esto es elegida: {elegida}")
    # # aquí planeo guardar lo que el jugador va develando
    # descubierto = len(elegida)*"_"
    descubierto = {i:"_" for i in range(len(elegida))}
    # print(f"esto es descubierto: {descubierto}")
    # print(alea)
    # # imprimir los espacios que ocupa la palabra y el mensaje de interacción con el usuario
    # input(f"""{descubierto}\n\nIngresa una letra: """)
    # # pedirle al usuario que ingrese una letra hasta que adivine


    # # temporalmente mostramos la palabra aleatoria
    palabra = {i:a for i,a in enumerate(elegida)}
    # print(f"esto es palabra: {palabra}")

    # estado = palabra == descubierto

    # print(f"son iguales la elegida y la descubierta? {estado}")

    # # contador de oportunidades:
    OPORTUNIDADES = 5

    # # aquí empezamos a jugar
    while OPORTUNIDADES > 0 and palabra != descubierto:
        # # limpiando la pantalla
        os.system("clear")
        # print(f"OPORTUNIDADES vale: {OPORTUNIDADES}")
        print(f"\nOportunidades restantes: {OPORTUNIDADES}\n")
        CUENTA = 0
        # print(f"CUENTA vale: {CUENTA}")
        for i in descubierto.values():
            print(i, end=" ")
        letra = input("""\n\nIngresa una letra: """)
        for i,a in palabra.items():
            # print(f"{i}:{a}")
            if letra.upper() == palabra[i]:
                # # si esto es verdad, debemos alterar a "descubierto"
                # print("sí")
                # # con esta línea sustituimos
                descubierto[i] = letra.upper()
                CUENTA += 1
        # print(f"ahora CUENTA vale: {CUENTA}")
        if CUENTA == 0:
            OPORTUNIDADES -= 1
            print(f"\n¡Error! Te quedan {OPORTUNIDADES} oportunidades\n")
        # print(f"ahora OPORTUNIDADES vale: {OPORTUNIDADES}")

    if OPORTUNIDADES == 0:
        print(f"¡PERDISTE! La palabra era {elegidaNato} ")
    elif palabra == descubierto:
        # for i in descubierto.values():
        #         print(i, end="")
        print(f"¡GANASTE! La palabra es {elegidaNato}")



if __name__ == "__main__":
    # # inicio
    run()