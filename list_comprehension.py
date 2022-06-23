#Lista de los numeros que no sean divisibles entre 3
def run():
    # numbers=[]
    # for i in range (1,101):
    #     if i % 3 != 0:
    #         i= i**2
    #         numbers.append(i)

    #element for element in iterable if condition
    numbers=[i**2 for i in range(1,101) if i%3 != 0]
    print("Lista final:", numbers)

    print("\n List comprehensions de todos los multiplos de 4 que a su vez son multiplos de y 9 hasta de 5 digitos")
    new_numbers=[i for i in range (1, 100000) if i%4 == 0 and i%6 == 0 and i%9 == 0]
    print("Resultado:", new_numbers)



if __name__ == '__main__':
    run()