import random
user_result = 0
bot_result = 0

i = 1
safe_word = 'koniec'

GAME_RANGE = ['k', 'p', 'n', 'j', 's']
WINNERS = {
    'k' : ['n' , 'j'],
    'p' : ['k', 's'],
    'n' : ['j', 'p'],
    'j' : ['p', 's'],
    's' : ['n', 'k']
}


def get_comp_choice():
    return random.choice(GAME_RANGE)

def games_num():
    games = (input('Wprowadź liczbę gier: '))
    while not games.isdigit():
        games = (input('Zły format!: Wprowadź poprawną liczbę gier: '))
    else:
        games = int(games)
    return games

def user_answer():
    x = input('Wprowadź k/p/n/j/s: ')
    while x not in GAME_RANGE:
        x = input('Zły input! Wprowadź k/p/n/j/s: ')
    return x

def show_result(comp, user):
    if comp == user:
        print('remis ')
    elif comp in WINNERS[user]:
        print('Wygrałeś.')
    else:
        print('Przegrałeś')

def main():
    user = ' '
    while True:
        comp = get_comp_choice()
        user = user_answer()
        print(f'{comp}, {user}')
        show_result(comp, user)
        play_again = input('Grasz dalej? T/N').upper()

        if play_again == 'N':
            print('KONIEC GRY')
            break


main()