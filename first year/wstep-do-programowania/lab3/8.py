"""
Napisz skrypt, który wyświetli gwiazdki jak poniżej. Liczba wierszy (lub gwiazdek w
linii) powinna być podawana przez użytkownika.
Przykład: 3
* * *
* * *
* * *
"""

liczba = int(input("liczba? "))
for x in range(liczba):
    for y in range(liczba):
        print('*', end="")
    print("")