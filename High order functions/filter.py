lista = [1,2,3,4,5,6,7,8,9,10]

#filtrar impares de la lista y eso mandarlo a una nueva lista en newlist
newlist =list(filter(lambda x: x%2 !=0, lista))

print(newlist)