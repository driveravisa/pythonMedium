def divisors(number):
        divisors = []
        for i in range (1,number +1):
            if number % i == 0:
                print(i, " Es divisor de ", number)
                divisors.append(i)
        return divisors


def run():
    number = input("Ingresa un número: ")
    assert number.isnumeric() and number.isnumeric() > 0, "Error, solo ingresa números mayores a 0"
    #assert number  > 1, "Ingresa un número mayor a 0"
    print(divisors(int(number)))
    print("Programa terminado")




if __name__ == '__main__':
    run()