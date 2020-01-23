a = 9

for i in range(5):
    print (a, end=" ")
    a -= 2

print()

lista =[]
b = 1
lista.insert(0,b)

for x in range(4):
    lista.append(lista[x] + 2)
lista.reverse()
for i in range(len(lista)):
    print(lista[i], end=" ")

print()

lista =[]
for x in range(5):
    if x == 0:
        lista.append(9)
    else:
        lista.append(lista[-1] - 2)
for i in range(len(lista)):
    print(lista[i], end=" ")

