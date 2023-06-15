def closure():
    txt = 'la'
    def inside(number):
        return txt * number

    return inside


var = closure()
result = var(2)
print(result)