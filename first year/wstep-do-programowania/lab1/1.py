"""
zadanie 1
Napisz skrypt, który pobiera długości boków prostokąta, a następnie oblicza jego pole i
obwód oraz wyświetla wyniki na ekranie.
"""
bokA = float(input("długość boku a: "))
bokB = float(input("długość boku b: "))

pole = bokA * bokB
obwod = 2 * bokA + 2 * bokB

odp = f'pole = {pole}\nobwod = {obwod}'
print(odp)