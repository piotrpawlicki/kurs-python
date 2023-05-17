def is_card_num(a):
    return a.isdigit()

def get_card_num():
    while True:
        card_nr = input('Insert card num here: ')
        if is_card_num(card_nr):
           # print('Proper card number')
            return card_nr
            break
        else:
            print('Wrong card number ')
            print('Try again')

def visa(number):
    return str(number).startswith('4') and len(number) in (13, 16)

def amex(number):
    return str(number).startswith('3') and len(number) == 15 and number[1] in ('4', '7')

def master_card(number):
    return len(number) == 16 and (
        int(number[0:2]) in range(51,56) or
        2221 <= int(number[:4]) <= 2720
    )

card_num = get_card_num()

if is_card_num(card_num):
    if visa(card_num):
        print('Visa')
    elif amex(card_num):
        print('Amex')
    elif master_card(card_num):
        print('MasterCard')
    else:
        print('Unknown card type')
