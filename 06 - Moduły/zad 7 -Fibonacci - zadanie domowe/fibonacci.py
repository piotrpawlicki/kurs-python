def fibonnacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnacci(n-1) + fibonnacci(n-2)

def whole_seq(n):
    fib_list = []
    luc_list = []
    tet_list = []
    for i in range(n):
        fib_list.append(fibonnacci(i))
        luc_list.append(lucas(i))
        tet_list.append(tetranacci(i))
    f = ', '.join(map(str, fib_list))
    l = ', '.join(map(str, luc_list))
    t = ', '.join(map(str, tet_list))
    return f, l, t

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def tetranacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return tetranacci(n-1) + tetranacci(n-2) + tetranacci(n-3) + tetranacci(n-4)


def main():
    n = input('Please insert number: ')
    while True:
        try:
            n = int(n)
            break
        except ValueError:
            n = input('Please insert a number: ')

    f, l, t = whole_seq(n)
    print(f'Fibonacci sequence: {n}  = {f}')
    print(f' Lucas sequence: {n} = {l}')
    print(f' Tetranacci sequence: {n} = {t}')


# if __name__ == '__main__':
#     main()
main()