DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    all_python_names = [i["name"] for i in DATA if i["language"] == "python"] #extraer trabajadores que escriban python
    all_platzi_names = [i["name"] for i in DATA if i["organization"] == "Platzi"] #extraer trabajadores que trabajen en platzi
    all_is_mayors = list(filter(lambda x: x["age"] > 17, DATA)) #extraer trabajadores que sean mayores (genera un nuevo script)
    all_is_mayors = list(map(lambda x: x["name"], all_is_mayors)) #extraer solo los nombres del script de trabajadores mayores
    #olders = list(map(lambda worker: {**worker, **{"old": worker["age"] > 70}}, DATA)) #Agregar nuevo campo OLD al diccionario si es mayor

    for i in DATA:
        if i["age"] > 70:
            print(i["name"]," es mayor")
            i["old"]=True
        else:
            i["old"]=False


    for i in DATA:
        print(i)

if __name__ == '__main__':
    run()