def is_even(number):
    if number % 2 == 0:
        result = 'even'
    else:
        result = 'not even'
    print(f'{number} is {result}')


a = input('Insert number: ')

while True:
    try:
        a = int(a)
        break
    except ValueError:
        a = input('Type error. Insert number: ')

is_even(a)
