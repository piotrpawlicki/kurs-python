
def bmi(height, weight):
    height = float(height.replace(".", ","))
    weight = float(weight.replace(",", "."))
    result = round(weight/(height**2), 2)
    return result


print('Your height in meters: ')
height = input()
print('Your weight in kg: ')
weight = input()

my_bmi = bmi(height, weight)

print('Your BMI is:', my_bmi)

