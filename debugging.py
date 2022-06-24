def divisors(number):
    try:
        if number < 1:
            raise ValueError("Ingresa un número mayor a 0")
        divisors = []
        for i in range (1,number +1):
            if number % i == 0:
                print(i, " Es divisor de ", number)
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)


def run():
    while True:
        try:
            number = int(input("Ingresa un número: "))
            print(divisors(number))
            print("Programa terminado")
        except ValueError:
            print("Debes ingresar un número")




if __name__ == '__main__':
    run()