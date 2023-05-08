while True:
    try:
        a = input('Input Value in range 4 - 10: ')
        a = int(a)
        if a in range(4, 11):
            break
    except ValueError:
        print('Value error')

for num in range(1, a+1):
    star = num * '*'
    print(star)
