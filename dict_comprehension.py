#crear diccionario con los llave de los 100 primeros numeros y su valor al cubo con list comprehension
#Lista de los numeros que no sean divisibles entre 3
def run():
    numbers={i: i**3 for i in range(1,101) if i%3 != 0}
    print(numbers)

    #Crear un dictionary comprehension cuyas llaves sean los 1000 primeros numeros naturales y sus raicen sean su valor
    print("Dictionary comprehension cuyas llaves sean los 1000 primeros numeros naturales y sus raicen sean su valor")
    new_numbers={i:round(i**0.5, 3) for i in range(1,101)}
    print(new_numbers)


if __name__ == '__main__':
    run()