import random, os

def run():
    os.system("clear")
    data = []
    with open("./data.txt", "r", encoding="utf-8") as word:
        for i in word:
            width = len(i) - 1
            data.append(i[:width])
    # print(data)
    origin = {n:data[n] for n in range(len(data))}
    # print(origin)
    # elegir una palabra aleatoriamente desde origin:
    # print(len(data))
    alea = random.randint(0,len(data))
    elegida = origin[alea]
    # print(alea)
    input(f"""{len(elegida)*"_ "}\n\nIngresa una letra: """)

    


if __name__ == "__main__":
    run()