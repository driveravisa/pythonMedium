def run():
    numbers=[]
    for i in range (1,11):
        i= i**2
        numbers.append(i)
        print("Procesando: ", numbers)
    print("Lista final:", numbers)

if __name__ == '__main__':
    run()