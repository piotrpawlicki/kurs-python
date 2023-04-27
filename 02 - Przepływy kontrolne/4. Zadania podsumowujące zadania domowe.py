import random

## zad1
print('***********************************')
print('Zad1')

names = input('Wprowadź imiona i rozdziel je przecinkiem: ').replace(' ',",")
list_names = names.split(',')

for i in list_names:
    print('Hello',i)
########################################################################################
## Zad2 - za pomocą 2 pętli
print('***********************************')
print('Zad2 - za pomocą 2 pętli')

txt = input('Insert text: ')
len_txt = len(txt)
txt_new=[]
for i in range (1, len_txt):
    if i % 2 == 1:
        txt_new.append(txt[i])
txt = ''.join(txt_new)
print(txt)

########################################################################################
## zad2
print('***********************************')
print('Zad2 - za pomocą 1 pętli')

txt = input('Insert text: ')
len_txt = len(txt)
txt_new=[]
for i in range (1, len_txt, 2):
    txt_new.append(txt[i])
txt = ''.join(txt_new)
print(txt)

########################################################################################
## zad2 - string slicing
print('***********************************')
print('Zad2 - string slicing')

txt = input('Insert text: ')
txt=txt[1::2]
print(txt)

########################################################################################
## zad3
print('***********************************')
print('Zad3')

lower_letters = 0
upper_letters = 0
digits = 0
other_chars = 0

txt = input('Enter text: ')

for i in txt:
    if i.isupper():
        upper_letters += 1
    elif i.islower():
        lower_letters += 1
    elif i.isdigit():
        digits += 1
    else:
        other_chars += 1
print('lower_letters: ', lower_letters)
print('upper_letters ', upper_letters)
print('digits ', digits)
print('other_chars ', other_chars)

########################################################################################
## zad4
print('***********************************')
print('Zad4')

game_range = ['k', 'p', 'n']
user_result = 0
bot_result = 0
i = 1
safe_word = 'koniec'
games = (input('Wprowadź liczbę gier: '))

while not games.isdigit():
    games = (input('Zły format!: Wprowadź poprawną liczbę gier: '))
else:
    games = int(games)

while i <= games:
    user = input('Wprowadź k/p/n: ')
    if user == safe_word:
        print('Koniec gry')
        break
    while user not in game_range:
        user = input('Zły input! Wprowadź k/p/n: ')
    bot = random.choice(game_range)
    if bot == 'k':
        if user == 'k':
            print('remis')
        elif user == 'p':
            print('Wygrałeś rundę!')
            user_result += 1
        else:
            print('Przegrałeś rundę! ')
            bot_result += 1
    elif bot == 'p':
        if user == 'p':
            print('remis rundę')
        elif user == 'n':
            print('Wygrałeś rundę!')
            user_result += 1
        else:
            print('Przegrałeś rundę! ')
            bot_result += 1
    else:
        if user == 'n':
            print('remis')
        elif user == 'k':
            print('Wygrałeś rundę!')
            user_result += 1
        else:
            print('Przegrałeś rundę! ')
            bot_result += 1
    i += 1
if bot_result > user_result:
    print(f'Wygrał komputer wynikiem {bot_result} : {user_result}')
elif bot_result < user_result:
    print(f'Wygrałeś wynikiem {user_result} : {bot_result}')
else:
    print(f'Mamy remis! {user_result} : {bot_result}')

########################################################################################
## zad5

bot = random.randrange(1,100)
max_games = 6
game_nr = 1
last_guess = 0

while game_nr < max_games:
    user = input('Zgadnij liczbę którą wylosował komputer: ')
    if user.isdigit() and (int(user) in range(1, 100)):
        user = int(user)
        game_nr += 1
        if user == bot:
            print('Wygrałeś')
            break
        elif game_nr == max_games:
            print(f'koniec gry. Szukałeś liczby {bot}')
        else:
            if last_guess == 0:
                last_guess = user
                if abs(last_guess-bot) < abs(last_guess - 0):
                    print('Ciepło! spróbuj raz jeszcze')
                else:
                    print('Zimno! spróbuj raz jeszcze')
            elif abs(last_guess - bot) > abs(user-bot):
                print('Ciepło! spróbuj raz jeszcze')
                last_guess = user
            elif abs(last_guess - bot) < abs(user-bot):
                last_guess = user
                print('Zimno! spróbuj raz jeszcze')
    else:
        print('Zły format!')