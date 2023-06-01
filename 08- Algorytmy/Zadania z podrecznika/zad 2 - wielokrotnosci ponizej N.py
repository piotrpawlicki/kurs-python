def get_number():
    while True:
        x = input('Wprowadx liczbe: ')
        try:
            x = int(x)
            return x
        except ValueError:
            print('To nie jest liczba')


def divided_by_5(user_number):
    i = 1
    five_list=[]
    while i * 5 < user_number:
        five_list.append(i * 5)
        i += 1
    return five_list

def divided_by_7(user_number):
    i = 1
    seven_list = []
    while i * 7 < user_number:
        seven_list.append(i * 7)
        i += 1
    return seven_list

def sum_all(list_of_numbers):
    sum = 0
    for i in list_of_numbers:
        sum += i
    return sum
def main():
    x = get_number()
    five = divided_by_5(x)
    seven = divided_by_7(x)
    all = set(seven + five)
    all = sum_all(all)
    print(all)

if __name__ == '__main__':
    main()