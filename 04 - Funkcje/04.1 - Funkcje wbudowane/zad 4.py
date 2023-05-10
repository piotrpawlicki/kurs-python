def is_even(number):
    if number % 2 == 0:
        result = 'even'
    else:
        result = 'not even'
    return result


number_list = [1, 2, 3, 4, 5, 6, 15, 189, 135,12]
for elem in range(0, len(number_list)):
    if is_even(number_list[elem]) == 'even':
        print(number_list[elem])
