a = int(input("Podaj pierwszą liczbę całkowitą: "))  # pobranie od użytkownika pierwszej wartości całkowitej
b = int(input("Podaj drugą liczbę całkowitą: "))     # pobranie od użytkownika drugiej wartości całkowitej

if a == b:
    print(a, "==", b)
elif a > b:
    print(a, ">", b)
else:
    print(a,"<", b)
