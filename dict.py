#crear diccionario con los llave de los 100 primeros numeros y su valor al cubo
def run():
    data={}
    for i in range(1,101):
        if i%3 != 0:
            data[i] = i**3
    print(data)

if __name__ == '__main__':
    run()