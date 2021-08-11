import random, sys


def run():
    print("Estoy pensando en un número entre 1 y 20.\n")
    rand = random.randint(1,21)
    while True:
        try:
            guess = int(input("Adivina cuál es: "))
            if guess < rand:
                print("El número es muy bajo")
            elif guess > rand:
                print("El número es muy alto")
            elif guess == rand:
                print(f"Buen trabajo, pensé en {guess}")
                sys.exit()
        except ValueError:
            print("Debes elegir un número")


if __name__ == '__main__':
    run()