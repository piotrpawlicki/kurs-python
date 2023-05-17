import random
def is_in_range():
    c = random.randint(1, 100)
    a = int(input('Insert min '))
    b = int(input('Insert max '))
    result = True if ((c > a) and (b > c)) else False
    return result


if is_in_range():
    print('Number in range')
else:
    print('Not in range')