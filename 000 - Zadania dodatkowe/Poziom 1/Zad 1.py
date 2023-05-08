while True:
    try:
        a = input('podaj liczbe a: ')
        a = int(a)
        b = input('podaj liczbe b: ')
        b = int(b)
        break
    except ValueError:
        print('Zły typ.')

c = a * b

if a  < 0 or b < 0:
    print('Nie mnożę, jedna z liczb jest ujemna ')
else:
    print(f'Wynik mnożenia a i b to : {c}')