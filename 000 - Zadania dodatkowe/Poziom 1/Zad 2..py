while True:
    try:
        a = input('Input Value: ')
        a = int(a)
        break
    except ValueError:
        print('Value error')

print(f'User input: {a}')
for num in range(1,11):
    b = a * num
    print(f' {a} * {num} = {b}')