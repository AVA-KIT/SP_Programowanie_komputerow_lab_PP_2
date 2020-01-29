p = list(range(1,21)) #Tworzymy przedział <1,20>

#Szukamy liczb z przedziału "p", które dzielą się bez reszty przez 3 
for i in p:
    if i % 3 == 0:
        print(i)
