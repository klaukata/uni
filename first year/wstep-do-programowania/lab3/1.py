"""
zadanie 1
Napisz skrypt, który pobierze od użytkownika dwie liczby całkowite. Następnie
zaczynając od mniejszej liczby, wypisze kolejne liczby aż do osiągnięcia wartości drugiej (większej) liczby.
Np. Wejście: 10, 5
Wyjście: 5, 6, 7, 8, 9, 10
"""
liczba_a = int(input("liczba a = "))
liczba_b = int(input("liczba b = "))

if liczba_b < liczba_a:
    liczba_a, liczba_b = liczba_b, liczba_a

while liczba_a <= liczba_b:
    print(liczba_a, end = ' ')
    liczba_a += 1