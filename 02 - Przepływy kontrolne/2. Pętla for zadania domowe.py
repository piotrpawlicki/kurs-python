
## zad1
print('***********************************')
print('Zad1')

items = ['latarka','zapalniczka','namiot']
for i in items:
    print(i)
print('Great, we are ready!')

########################################################################################
## zad2
print('***********************************')
print('Zad2')

items = ['oliwa','czosnek','chilli','makaron']
for i in items:
    print(i)
print('Podawaj na ciepło')

########################################################################################
## zad3
print('***********************************')
print('Zad3')

a = 0
for i in range(1,11):
    a = a + i
    print(a)

########################################################################################
## zad4
print('***********************************')
print('Zad4')

x = int(input('Wprowadź liczbę w zakresie od 0 do 8: '))
while x not in range(0,9):
    x = int(input('Błąd zakresu. Wprowadź liczbę w zakresie od 0 do 8: '))
if x == 0:
    print('0! = 1')
else:
    silnia = 1
    liczby = []
    for i in range(1,x+1):
        silnia *= i
        liczby.append(str(i))
    wynik = ' * '.join(liczby)
    print(f"{x}! =")
    print(f"{wynik} = {silnia}")


