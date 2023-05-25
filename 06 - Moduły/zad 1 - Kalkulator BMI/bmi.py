def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        answer = read_from_file('Underweight.txt')
    elif bmi < 25:
        answer = read_from_file('Normal.txt')
    elif bmi < 30:
        answer = read_from_file('Overweight.txt')
    else:
        answer = read_from_file('Obese.txt')
    return answer


def read_from_file(filename):
    with open(filename) as f:
        lines = f.read()
        return lines

