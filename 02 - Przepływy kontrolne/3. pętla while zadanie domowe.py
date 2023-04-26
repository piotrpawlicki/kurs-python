## zad1 pętla while
##C = 5/6(F-32)
print('***********************************')
print('Zad1')
F=0
while F < 201:
    C = 5 / 9 * (F - 32)
    print(C)
    F+=20

print('***********************************')
print('Zad1 - For')
F=0
for F in range(-1,201,20) :
    C = 5 / 9 * (F - 32)
    print(C)

print('***********************************')
print('Zad2')
secret_num = 6
user_num = int(input('Enter number: '))

while secret_num != user_num:
    user_num = int(input('Please try again: '))
while user_num == secret_num:
    print('Congrats!')
    break

