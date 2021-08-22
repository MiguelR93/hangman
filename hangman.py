import random, os

seis = """
    +-------+
    |       |
            |
            |
            |
            |
            |
            |
==============="""

cinco = """
    +-------+
    |       |
  (._.)     |
            |
            |
            |
            |
            |
==============="""

cuatro = """
    +-------+
    |       |
  (o_o)     |
    |       |
            |
            |
            |
            |
==============="""

tres = """
    +-------+
    |       |
  (O_O)     |
   /|       |
            |
            |
            |
            |
==============="""

dos = """
    +-------+
    |       |
  (O_O')    |
   /|\      |
            |
            |
            |
            |
==============="""

uno = """
    +-------+
    |       |
  (T_T)     |
   /|\      |
   /        |
            |
            |
            |
==============="""

cero = """
    +-------+
    |       |
  (x_x)     |
   /|\      |
   / \      |
            |
            |
            |
==============="""

salvado = """
    +-------+
    |       |
            |
            |
  Ufff!!!   |
 \(OoO)/    |
    |       |
   / \      |
===============
"""

def dibu(OPORTUNIDADES):
    if OPORTUNIDADES == 6:
        print(seis)
    elif OPORTUNIDADES == 5:
        print(cinco)
    elif OPORTUNIDADES == 4:
        print(cuatro)
    elif OPORTUNIDADES == 3:
        print(tres)
    elif OPORTUNIDADES == 2:
        print(dos)
    elif OPORTUNIDADES == 1:
        print(uno)
    elif OPORTUNIDADES == 0:
        print(cero)

def run():
    # creando una lista que contendrá las palabras del documento "data.txt"
    data = []
    # extrayendo las palabras de "data.txt"
    with open("./data.txt", "r", encoding="utf-8") as word:
        for i in word:
            width = len(i) - 1
            data.append(i[:width])


    origin = {n:data[n] for n in range(len(data))}

    # elegir una palabra aleatoriamente desde origin:
    elegidaNato = origin[random.randint(0,len(data))]
    elegidaA = elegidaNato.replace("á",'a')
    elegidaE = elegidaA.replace('é','e')
    elegidaI = elegidaE.replace('í','i')
    elegidaO = elegidaI.replace('ó','o')
    elegidaU = elegidaO.replace('ú','u')
    elegida = elegidaU.upper()

    # guarda lo que el jugador va develando:
    descubierto = {i:"_" for i in range(len(elegida))}

    letrasAdmitidas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    palabra = {i:a for i,a in enumerate(elegida)}

    letrasUsadas = []

    # contador de oportunidades:
    OPORTUNIDADES = 6

    # Game begin
    while OPORTUNIDADES > 0 and palabra != descubierto:
        os.system("clear")
        print(letrasUsadas)
        dibu(OPORTUNIDADES)
        CUENTA = 0
        for i in descubierto.values():
            print(i, end=" ")
        letra = input("""\n\nIngresa una letra: """)
        # evaluando que lo registrado sea una letra:
        CONTADORDELETRASADMITIDAS = 0
        for i in letrasAdmitidas:
            if letra != i:
                CONTADORDELETRASADMITIDAS += 1
        if CONTADORDELETRASADMITIDAS > 26:
            print("eso no era una letra")
            input("persiona enter")
            continue
        
        LETRAREPETIDA = 0
        # la letra ya fue usada?
        for i in letrasUsadas:
            if i == letra:
                print("esta letra ya fue usada")
                input("presione enter")
                LETRAREPETIDA += 1
                break
        
        # reiniciar si ya se usó la letra:
        if LETRAREPETIDA > 0:
            continue
        else:
            for i,a in palabra.items():
                if letra.upper() == palabra[i]:
                    descubierto[i] = letra.upper()
                    CUENTA += 1
            if CUENTA == 0:
                OPORTUNIDADES -= 1
            letrasUsadas.append(letra)
    

    os.system("clear")

    if OPORTUNIDADES == 0:
        print(letrasUsadas)
        dibu(OPORTUNIDADES)
        print(f"\n¡PERDISTE! La palabra era {elegidaNato}.")
    elif palabra == descubierto:
        print(letrasUsadas)
        print(salvado)
        print(f"\n¡GANASTE! La palabra es {elegidaNato}.")



if __name__ == "__main__":
    run()