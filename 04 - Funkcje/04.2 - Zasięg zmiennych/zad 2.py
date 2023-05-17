def min_of_2(a,b):
    return a if a < b else b


def min_of_3(a,b,c):
    return min_of_2(c, min_of_2(a,b))


print(min_of_3(1,3,3))
