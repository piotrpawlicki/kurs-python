import io


def open_file(filename):
    with open(filename, 'r') as f:
        return f.read()


def read_file_with_w(filename):
    try:
        with open(filename, 'w') as f:
            return f.readlines()
    except io.UnsupportedOperation as e:
        print(e)
    finally:
        with open(filename, 'r') as f:
            return f.readlines()


def create_file(filename):
    try:
        with open(filename, 'x') as f:
            return f.write('Hello World')
    except FileExistsError as e:
        print(e)
    finally:
        print('File created or Exist')


def main():
    create_file('test.txt')
    print(open_file('test.txt'))
    print(read_file_with_w('test.txt'))


if __name__ == '__main__':
    main()