import random
answers = ['N', 'Y']
flip_again = 'Y'
result_list = ['🦅',  '🪙']
while flip_again == 'Y':
    result = random.choice(result_list)
    print(f'Coin flip result = {result}')
    flip_again = input('Do you want to flip again? (Y/N): ').upper()
    while flip_again not in answers:
        print('Wrong answer. You can put only Y or N')
        flip_again = input('Do you want to flip again? (Y/N): ').upper()
if flip_again == 'N':
    print('Game over')