test_list = [1,'2',{3,'4'}]

print(test_list)

def my_function(test_list):
    #raise TypeError('custom error')
    for elem in test_list:
        x = 10/elem
        print(x)

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


if __name__ == '__main__':
    main()