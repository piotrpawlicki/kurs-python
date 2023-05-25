def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

if __name__ == '__main__':
    print(max_of_three(1, 2, 3))