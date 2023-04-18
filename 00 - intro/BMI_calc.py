print('Your height in meters: ')
height = input()
height = height.replace(".", ",")
height = float(height)

print('Your weight in kg: ')
weight = input()
weight = weight.replace(",", ".")
weight = float(weight)

BMI = weight/(height**2)
BMI = round(BMI, 2)

print('Your BMI is:', BMI)
