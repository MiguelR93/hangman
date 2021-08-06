def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input("Ingresa un número: ")) #user type a number
        assert num > 0, "Debes ingresar un número positivo"
        print(divisors(num))
    except AssertionError as AE:
        print(AE)
        run()

if __name__ == '__main__':
    run()