value_list = [1,2,3,4,5,6,7,8,9,10]
def sum_elem(items):
    result = 0
    for i in items:
        result += i
    return result

print(sum_elem(value_list))