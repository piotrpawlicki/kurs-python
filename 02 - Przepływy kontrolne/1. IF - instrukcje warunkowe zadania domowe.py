
## zad1
print('***********************************')
print('Zad1')
number = int(input('Input number: '))
print('Twoja liczba jest podzielna przez 3') if number % 3 == 0 else 1==1

########################################################################################
## zad2
print('***********************************')
print('Zad2')
a = int(input('Input number a: '))
b = int(input('Input number b: '))

x = a + b
print(x) if x>100 else print('Koniec')

########################################################################################
## zad3
print('***********************************')
print('Zad3')

rev1 = int(input('Input first review: '))
rev2 = int(input('Input second review: '))
rev3 = int(input('Input third review: '))

avg_rev = (rev1+rev2+rev3)/3

if avg_rev > 7:
    print('bardzo dobry')
elif avg_rev >5:
    print('przeciętna')
else:
    print('nie warta uwagi')
########################################################################################
## zad4
print('***********************************')
print('Zad4')

string = input('Wprowadź ciąg znaków: ')

if ('a' or 'A') in string and len(string) > 5:
    string_new = string.replace('a','z').replace('A','Z')
    print(string_new)
########################################################################################
## zad5
print('***********************************')
print('Zad5')

password = input('Wprowadź hasło: ')
len_pass = len(password)
is_1_up = password.islower()  ## The islower() method returns True if all alphabets in a string are lowercase alphabets. If the string contains at least one uppercase alphabet, it returns False.
is_1_low = password.isupper()
is_digit = password.isdigit() and password.isalnum()
is_alfa = password.isalpha() and password.isalnum()
if len_pass < 8:
    print('Za krótkie hasło')
if is_1_low:
    print('Brak wielkich liter')
if is_1_up :
    print('Brak małych liter')
if is_digit:
    print('Brak liter')
if is_alfa:
    print('Brak cyfr')
print(f'Twoje hasło to : {password}')

########################################################################################
## zad6
print('***********************************')
print('Zad6')

test_num = 10
number = int(input('Enter number in range 1-100: '))
while number > 100 or number < 1:
    number = int(input('Enter number in proper range 1-100: '))
if test_num == number:
    print('Gratulacje')
else:
    print('Nie udało się')

########################################################################################
## zad7
print('***********************************')
print('Zad7')

height = input('Your height in meters: ')
height = height.replace(",", ".")
height = float(height)

weight = input('Your weight in kg: ')
weight = weight.replace(",", ".")
weight = float(weight)

BMI = weight/(height**2)
BMI = round(BMI, 2)

if BMI > 30:
    result = 'Obese'
elif BMI > 25:
    result = 'Overweight'
elif BMI > 18.4:
    result = 'Normal range'
else:
    result = 'Underweight'

print('Your BMI is:', BMI, '     Your result is : ', result)
########################################################################################
## zad8
print('***********************************')
print('Zad8')

a = int(input('Enter number a: '))
b = int(input('Enter number b: '))
c = int(input('Enter number c: '))

abc=[a,b,c]
sorted_abc = sorted(abc, key = float)
print(sorted_abc)