print('***********************************')
print('Zad3\n\n')

n = input('Input number: ')
while True:
    try:
        n = int(n)
        break
    except ValueError:
        n = input('Value error!, Input number: ')

char = input('Input 1 char: ')

tab = [str(char) * n] * n

for row in tab:
    print(' '.join(row))