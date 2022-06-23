def run():
    list = [1, 'Hey', 2.8]
    dict = {
        "first_name": "Julian",
        "last_name": "García"
    }

    super_list=[
        {"first_name": "Julian", "last_name": "García"},
        {"first_name": "Maria", "last_name": "Morán"},
        {"first_name": "Carlos", "last_name": "Rodriguez"},
        {"first_name": "Esteban", "last_name": "Perez"},
        {"first_name": "Valeria", "last_name": "Gómez"},
    ]

    super_dict={
        "natural_numbers":[1,2,3,4,5],
        "integer_numbers":[-2,-1,0,1,2],
        "floating_numbers":[3.45, 49.4, 12.434]
    }

    print("Ciclo Diccionario con listas")

    for key, value in super_dict.items():
        print(key, " ===> ", value)

    print("Lista de diccionarios")

    for i in super_list:
        print(i["first_name"], i["last_name"])


if __name__ == '__main__':
    run()