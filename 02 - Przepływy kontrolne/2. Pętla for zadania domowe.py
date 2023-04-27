# zad1
print('***********************************')
print('Zad1')

items = ['latarka', 'zapalniczka', 'namiot']
for i in items:
    print(i)
print('Great, we are ready!')

########################################################################################
# zad2
print('***********************************')
print('Zad2')

items = ['oliwa', 'czosnek', 'chilli', 'makaron']
for i in items:
    print(i)
print('Podawaj na ciepło')

########################################################################################
# zad3
print('***********************************')
print('Zad3')

a = 0
result = []
for i in range(1, 12):
    result.append(str(a))
    a = a + i
str_result = ';'.join(result)
print(str_result)
########################################################################################
# zad4
print('***********************************')
print('Zad4')

x = input('Wprowadź liczbę w zakresie od 0 do 8: ')
while int(x) not in range(0, 9):
    x = int(input('Błąd zakresu. Wprowadź liczbę w zakresie od 0 do 8: '))
if x == 0:
    print('0! = 1')
else:
    silnia = 1
    liczby = []
    for i in range(1, x + 1):
        silnia *= i
        liczby.append(str(i))
    wynik = ' * '.join(liczby)
    print(f"{x}! =")
    print(f"{wynik} = {silnia}")

########################################################################################
# zad4
print('***********************************')
print('Zad4 - wersja druga')


def silnia(silnia_input):
    if silnia_input != 0:
        silnia_output: int = silnia_input * silnia(silnia_input-1)
        return silnia_output
    else:
        return 1


x = input('Wprowadź liczbę w zakresie od 0 do 8: ')
try:
    x = int(x)
    while x not in range(0, 9):
        x = int(input('Błąd zakresu. Wprowadź liczbę w zakresie od 0 do 8: '))
        continue
   ## break
except ValueError:
    print('Błąd formatu. Wprowadź liczbę w zakresie od 0 do 8: ')
    continue

a = silnia(x)
liczby = [str(i) for i in range(1, x+1)]  # do listy dodajemy kolejne elementy do wyświetlenia
wynik = ' * '.join(liczby)
print(f'{x}!=\n{wynik} = {a}')
