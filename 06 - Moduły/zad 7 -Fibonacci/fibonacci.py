def fibonnacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnacci(n-1) + fibonnacci(n-2)

def print_whole_fibonnacci(n):
    fib_list = []
    for i in range(n):
        add = fibonnacci(i)
        fib_list.append(add)
    s = ', '.join(map(str, fib_list))
    return s

def main():
    print(print_whole_fibonnacci(4))

if __name__ == '__main__':
    main()
