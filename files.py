def read():
    numbers = []
    with open("./files/numbers.txt","r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)



def write():
    names = ["Hugo", "Maria", "Fernando", "Esmeralda", "Rocío", "Juan"]
    with open("./files/names.txt","a", encoding="utf-8") as f2:
        for name in names:
            f2.write(name)
            f2.write("\n")




def run():
    read()
    write()

if __name__ == '__main__':
    run()