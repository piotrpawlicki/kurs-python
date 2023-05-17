'''
def maximum(a,b,c):
    if  (c <= a) and (b <= a) :
        result = a
    elif (c <= b) and (a <= b):
        result = b
    elif (a <= c) and (b <= c):
        result = c
    return result
'''


def max_of_2(a,b):
    return a if a > b else b


def max_of_3(a,b,c):
    return max_of_2(c, max_of_2(a,b))


print(max_of_3(1,3,3))
