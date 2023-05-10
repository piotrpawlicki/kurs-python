import math
def pole_kola(r):
    pole = math.pi * r**2
    return pole

r = input('Wprowadź promień koła ')
while True:
    try:
        r = float(r)
        break
    except TypeError:
        r = input('liczba to ma byc! Wprowadź promień koła')
pole = pole_kola(r)
print(f'pole kola to {pole}')