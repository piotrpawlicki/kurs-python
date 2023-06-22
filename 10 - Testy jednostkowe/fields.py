
def is_numeric(values):
    types = (int, float)
    for v in values:
        if not isinstance(v,types):
            raise ValueError("a and b must be numbers")

def rectangle(a,b):
    is_numeric((a,b))
    return a*b

    #print(a*b)
def triangle(a,b):
    is_numeric((a, b))
    return a*b/2

def trapezoid(a,b,h):
    is_numeric((a,b,h))
    return (a + b) * h / 2

def main():
    print(rectangle(10, 5) == 50)
    print(triangle(10, 5) == 25)
    print(rectangle(10, "*****"))

if __name__ == "__main__":
    main()