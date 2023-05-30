# while True:
#     x = input("Enter a number: ")
#     if x.isdigit():
#         x = float(x)
#         break
#     else:
#         print("Invalid input")

def my_function():
    #raise TypeError('custom error')
    x = 0
    return 'aaa' + x

def main():
    try:
        my_function()
    except ValueError as e:
        print(e)
        print('Błąd wartości')

    except (TypeError, ZeroDivisionError) as e:
        print('SUN')
        print(e)

    except:
        # handle all other exceptions
        print('No idea')

    print('LALALALALALALALALALALALALALALA')

if __name__ == '__main__':
    main()