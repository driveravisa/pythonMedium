#importar funcion reduce de functools
from functools import reduce

lista = [2,3,4,5]


#en primer iteracion x es el primer elemento de la lista(2) y 'y' el segundo(3) en la siguiente iteracion x es el resultado de la primera itecacion
#(2x3 = 6) y 'y' será el siguiente elemento de la lista '4' en la sig iteracion x = (6x4 = 24) 'y' es 5 dando como resultado 24x5 = 120
valor = reduce(lambda x,y: x*y, lista)

#for
lista2 = [2,3,4,5]
valor2=1
for i in lista2:
    valor2 = i*valor2


print(valor)
print(valor2)