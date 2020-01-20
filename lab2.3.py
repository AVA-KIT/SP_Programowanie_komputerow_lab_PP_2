diskSize = 250               #wielkość dysku w GB
diskSizeUsed = 125           #zajętego miejsca na dysku w GB

fileSize = int(input("Podaj wielkość pliku: ")) #wielkość pliku podanego przez użytkownika

if fileSize <= diskSize - diskSizeUsed:
    print("Pobranie pliku zakończone sukcesem")

print("Brak miejsca na dysku") 
