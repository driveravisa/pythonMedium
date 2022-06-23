palindromo = lambda texto: texto == texto[::-1]

text=input("ingresa palindromo: ")
palindromo('ana0')

if palindromo == True:
    print("SI es palindromo")
else:
    print("No es palindromo")

