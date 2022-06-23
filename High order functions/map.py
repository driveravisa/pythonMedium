lista = [1,2,3,4,5,6,7,8,9,10]

#elevar al cuadrado los numeros de lista

#map
newlist =list(map(lambda x: x**2, lista))

#list comprehension
newlist2 = [i**2  for i in lista]

#for
newlist3 =[]
for i in lista:
    newlist3.append(i**2)

print(newlist)
print(newlist2)
print(newlist3)