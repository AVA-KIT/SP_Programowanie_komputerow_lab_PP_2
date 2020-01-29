#Pierwszy sposób uzyskania ciągu
lista = ['1 a', '1 b', '1 c','2 a','2 b', '2 c', '3 a', '3 b', '3 c']

for i in lista:
    print(i)

print()

#Drugi sposób uzyskania ciągu
lista = ['a', 'b', 'c']

for i in lista:
    print(1, i)
for i in lista:
    print(2, i)
for i in lista:
    print(3, i)


print()

#Trzeci sposób uzyskania ciągu
lista1 = [1,2,3]
lista2 = ['a','b','c']

for i in range(3):
    print(lista1[0], lista2[i])

for i in range(3):
    print(lista1[1], lista2[i])

for i in range(3):
    print(lista1[2], lista2[i])

print()