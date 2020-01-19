chanels = {'Google':1480, 'Email':300, 'Natural Traffic':440, 'TV Spot':700} #obiekt dictionary o nazwie chanels 

print(chanels['Email'])

chanelsUpdate = {'Natural Traffic':520, 'News':600} #nowy słownik chanelsUpdate

chanels.update(chanelsUpdate) #Aktualizacja słownika chanels wartościami z chanelsUpdate

print(chanels.keys())

del chanels['Email'] #Usunięcie wartości 'Email' ze słownika


