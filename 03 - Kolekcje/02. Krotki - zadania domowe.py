########################################################################################
# Zad1

print('***********************************')
print('Zad1\n\n')

pupil = ('kot', 'europejski krótkowłosy', 'Mela')
zwierze, rasa, imie = pupil

print(f'Mój {zwierze} rasy {rasa} wabi się {imie}')


########################################################################################
# Zad2
print('***********************************')
print('Zad2\n\n')

k1 = (1, 2, 3, 4, 5, 6, 4, 'Ala', 5, 'Ala')
k1 = sorted(k1)
duplicates = []

for i in range(len(k1)-1):
    if k1[i] == k1[i+1]:
        duplicates.append(k1[i])
print(duplicates)
########################################################################################
# Zad3
print('***********************************')
print('Zad3\n\n')

krotka = (93, 4, 5, 6, 7, 8, 9)

while True:
    try:
        num = input('podaj liczbe: ')
        num = int(num)
        break
    except ValueError:
        print('Zły typ.')
if num in krotka:
    print(f'{num} jest w krotce po numerem {krotka.index(num)}')
else:
    print('Nie jest w krotce')
