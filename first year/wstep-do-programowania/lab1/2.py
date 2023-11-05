"""
zadanie 2
Napisz skrypt, który pobiera od użytkownika drogę pokonaną przez samochód oraz średnie
spalanie (w litrach na 100 km) i wyświetli informację o przewidywanym zużyciu paliwa oraz o szacowanych
kosztach podróży (cena paliwa 6.5 zł/l).
"""
droga = float(input("droga = "))
spalanie = float(input("srednie spalanie = "))

zuzycie = (droga * spalanie) / 100

cena_paliwa = 6.5
koszt_podrozy = zuzycie * cena_paliwa

print(koszt_podrozy)
