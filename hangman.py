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
    data = [] # it creates a list with words from data.txt // crea una lista que contendrá las palabras del documento "data.txt
    with open("./data.txt", "r", encoding="utf-8") as word: # It opens the data.txt document and gets words form it // extrayendo las palabras de "data.txt"
        for i in word:
            width = len(i) - 1
            data.append(i[:width])


    origin = {n:data[n] for n in range(len(data))} # dictionary with words from data // diccionario con palabras de data.txt
    elegidaNato = origin[random.randint(0,len(data))] # chose a random word from origin // elegir una palabra aleatoriamente desde origin:
    elegida = elegidaNato.replace("á",'a').replace('é','e').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').upper() # modifies the word to make it easier to understand for the program
    descubierto = {i:"_" for i in range(len(elegida))} # store words revelated by the player // guarda lo que el jugador va develando
    letrasAdmitidas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # valid characters
    palabra = {i:a for i,a in enumerate(elegida)} # It creates a dictionary with each character of the chosen word
    letrasUsadas = [] # store valid characters used by the player
    OPORTUNIDADES = 6 # chance's counter // contador de oportunidades


    # Game begin
    while OPORTUNIDADES > 0 and palabra != descubierto:
        os.system("clear")
        print(letrasUsadas)
        dibu(OPORTUNIDADES)
        CUENTA = 0
        for i in descubierto.values():
            print(i, end=" ")
        letra = input("""\n\nIngresa una letra: """)
        CONTADORDELETRASADMITIDAS = 0 # Counter for valid characters in every loop; it must be lower than 27
        for i in letrasAdmitidas:
            if letra != i:
                CONTADORDELETRASADMITIDAS += 1
        if CONTADORDELETRASADMITIDAS > 26:
            print("eso no era una letra")
            input("persiona enter")
            continue
        
        LETRAREPETIDA = 0 # It increase if the characters has been used before
        for i in letrasUsadas:
            if i == letra:
                print("esta letra ya fue usada")
                input("presione enter")
                LETRAREPETIDA += 1
                break
        
        if LETRAREPETIDA > 0: # It restart the loop if the character has been used before // reiniciar si ya se usó la letra
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