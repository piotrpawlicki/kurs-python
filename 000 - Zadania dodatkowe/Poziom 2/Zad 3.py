import random

a = 0 #random.randint(1, 101)
b = 1 #random.randint(1, 101)
tries = 1
answers = ['W', 'N']
answer = 'N'
while ((a < b) and answer == 'N') or ((a > b) and answer == 'W'):
    a = random.randint(1, 101)
    b = random.randint(1, 101)
    answer = input(f'Zgadnij, czy kolejna wylosowana liczba jest wyższa czy niższa niż {a} (W/N):  ').upper()
    while answer not in answers:
        print('Zła odpowiedźr. Wprowadź tylko W lub N')
        answer  = input(f'Zgadnij, czy kolejna wylosowana liczba jest wyższa czy niższa niż {a} (W/N):  ').upper()
    if a > b and answer == 'W':
        print('Przegrałeś. Próbuj do skutku')
        tries +=1
    elif a < b and answer == 'N':
        print('Przegrałeś. Próbuj do skutku')
        tries +=1
    else:
        break

print(f'Gratuluję, wygrałeś w {tries} próbach. Porównywałeś {a} i {b} ')