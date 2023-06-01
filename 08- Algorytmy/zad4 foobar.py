def foo_bar(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FooBar")
        elif i % 3 == 0:
            print("Foo")
        elif i % 5 == 0:
            print("Bar")
        else:
            print(i)


def get_number():
    while True:
        x = input('Wprowadz liczbe: ')
        try:
            x = int(x)
            return x
        except ValueError:
            print('To nie jest liczba')

def main():
    x = get_number()
    foo_bar(x)

if __name__== "__main__":
    main()