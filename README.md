# SP_Programowanie_komputerow_lab_PP_2
Studia podyplomowe Podstawy programowania - Python, Wydział Informatyki, ZUT w Szczecinie
Laboratorium 2: Listy, krotki, słowniki, instrukcja warunkowa, pętle

Zadanie 1 - plik lab2.1.py -
Organizujemy listę przebojów.
1. Utwórz listę hitsTitles zawierającą tytuły: 'BROTHERS IN ARMS','BOHEMIAN
RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE
HERE'
2. Dodaj do listy kolejne dwie piosenki: 'CHILD IN TIME' i 'AGAIN'
3. Wygląda na to, że w systemie głosowania była luka. Na pozycji 3 powinna się
znaleźć piosenka 'HOTEL CALIFORNIA'
4. Ops... wygląda na to, że system był bardziej zepsuty... oczywiście to wina IT.
Piosenka 'THE SOUND OF SILENCE' powinna znaleźć się na pierwszym miejscu
5. To na jakiej pozycji jest teraz 'HOTEL CALIFORNIA'? Odnajdź numer indeksu dla
tej piosenki
6. A jednak 'HOTEL CALIFORNIA' powinien zostać usunięty z listy
7. No i na pierwszym miejscu tytuł "THE SOUND OF SILENCE" powinien zostać
zamieniony na "ENJOY THE SILENCE"
8. Utwórz kopię listy, która będzie służyła do odczytania przebojów na antenie. Nowa
lista ma nazywać się hitsToRead
9. Odwróć kolejność elementów na liście hitsToRead.
10. Posortuj hitsToRead w kolejności alfabetycznej
11. Prowadzący listę przebojów po odczytaniu tytułu usuwa z listy hitsToRead
odczytany element. Dlatego korzysta z metody pop :). Zasymuluj odczyt dwóch
pierwszych pozycji
12. W czasie audycji słuchacze domagali się aby zagrać dodatkowo 'NOTHING
COMPARES 2 U' i 'WISH YOU WERE HERE'. Utwórz listę additionalSongs
zawierającą te dwa tytuły.
13. Dodaj do listy hitsToRead elementy z listy additionalSongs
14. Ile razy będzie zagrane 'WISH YOU WERE HERE' a ile razy 'RIDERS ON THE
STORM'. Wyświetl ile razy te piosenki występują na liście hitsToRead.
15. Audycja się kończy. Wyczyść listę hitsToRead

Zadanie 2 - plik lab2.2.py -
Analizujesz wydajność kanałów, jakimi można dotrzeć do klientów. Każdorazowo po
zmianie słownika wyświetl jego zawartość.
1. Utwórz obiekt dictionary o nazwie chanels z następującymi kluczami i
wartościami:
• Google - 1480
• Email - 300
• Natural Traffic - 440
• TV Spot - 700
2. Wyświetl wartość skojarzoną z kluczem "Email"
Utwórz nowy słownik chanelsUpdate z kluczami i wartościami:
• Natural Traffic - 520
• News - 600
4. Zaktualizuj słownik chanels wartościami z chanelsUpdate
5. Wyświetl wszystkie klucze z chanels
6. Usuń wartość 'Email' ze słownika

Zadanie 3: (if – else) - plik lan2.3.py -
Twój zespół opracowuje przeglądarkę internetową w Pythonie! Twoim zadaniem jest
sprawdzenie czy operacja pobierania pliku na dysk ma szansę się udać, czy jest od razu
skazana na porażkę ze względu na brak miejsca na dysku. Wykorzystaj zmienne: diskSize
- zmienna numeryczna (np. o wartości np. 140) oznaczająca wielkość dysku w GB,
diskSizeUsed - zmienna numeryczna (np. o wartości np. 100) oznaczająca ilość zajętego
miejsca na dysku w GB, fileSize - zmienna numeryczna (oznaczająca wielkość
pobieranego pliku w GB), do której pobierzesz wartość od użytkownika.
Napisz skrypt, wykorzystując polecenie IF, które w przypadku, gdy jest wystarczająco
wolnego miejsca na dysku wyświetli komunikat "Pobranie pliku zakończone sukcesem".
W przypadku, gdy plik jest za duży, ma być wyświetlony komunikat o braku miejsca na
dysku.

Zadanie 4: (if – elif – else) - plik lab2.4.py -
Napisz program, który pobierze od użytkownika dwie wartości całkowite. Sprawdź, która
wartość jest większa i wyświetl właściwy komunikat, podając pobrane wartości, np. dla
wartości 4 i 6, wyświetl: 4 < 6, a dla wartości 4 i 4 wyświetl, że 4 == 4.

Zadanie 5 - plik lab2.5.py -
Napisz program, który będzie sprawdzał czy podana przez użytkownika liczba jest
parzysta czy nieparzysta. Jako wynik powinien pojawić́ się̨ komunikat z odpowiednią
informacją.

Zadanie 6 plik lab2.6.py -
Napisz skrypt, który wyświetli poniższy ciąg wartości:
0 1 2 3 4 5
przy pomocy:
• pętli for
• pętli while
• pętli for wspartej listą, która będzie zawierała w/w wartości

Zadanie 7 plik lab2.7.py -
Napisz skrypt, który wyświetli ciąg wartości: 9 7 5 3 1, przy pomocy pętli for,
wykorzystując 3 różne sposoby. W wyniku na ekranie mają pojawić się trzy ciągi, każdy
w osobnej linii.

Zadanie 8 plik lab2.8.py -
Wykorzystując trzy różne sposoby, proszę za pomocą pętli for uzyskać poniższy ciąg:
1 a
1 b
1 c
2 a
2 b
2 c
3 a
3 b
3 c
W wyniku na ekranie mają pojawić się trzy ciągi (zgodne ze wzorem), oddzielone jedną
pustą linią.

Zadanie 9 plik lab2.9.py -
Proszę utworzyć listę a = [1, 2, 3, 4, 5, 6, 7, 8] nie używając pętli ale używając funkcji
range(). Następnie przy pomocy pętli for wyświetl tylko wartości od 1 do 4, zgodnie ze
wzorem.
Moja lista: [1, 2, 3, 4, 5, 6, 7, 8]
----------------
1
2
3
4

Zadanie 10 plik lab2.10.py -
Proszę znaleźć wszystkie liczby z przedziału <1,20>, które dzielą się bez reszty przez 3.
3
6
9
12
15
18
