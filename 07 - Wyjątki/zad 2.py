value_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def get_number(message):
    while True:
        x = input(message)
        try:
            x = int(x)
            return x
        except ValueError as e:
            print(e)


def main():
    x = get_number('Insert Tuple index: ')
    a = get_number('Insert Tuple new value: ')

    try:
        value_tuple[x] = a
    except (IndexError, TypeError) as e:
        print(e)


if __name__ == "__main__":
    main()