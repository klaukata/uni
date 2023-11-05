'''
Zadanie 1
• Dla osób poniżej 4 roku życia wstęp jest bezpłatny.
• Dla osób w wieku od 4 do 18 lat bilet kosztuje 10zł.
• Dla osób powyżej 18 roku życia bilet kosztuje 20
'''

wiek_klienta = int(input("wiek klienta: "))

if wiek_klienta < 4:
    cena_biletu = 0
elif wiek_klienta <= 18:
    cena_biletu = 10
elif wiek_klienta > 18:
    cena_biletu = 20

print(f'cena biletu: {cena_biletu}')