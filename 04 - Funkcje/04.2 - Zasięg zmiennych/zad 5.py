import random

def cieplo_zimno(max_games):
    bot = random.randrange(1,100)
    #max_games = 6
    game_nr = 0
    last_guess = 0

    while game_nr <= max_games:
        user = input('Zgadnij liczbę którą wylosował komputer: ')
        if user.isdigit() and (int(user) in range(1, 100)):
            user = int(user)
            #game_nr += 1
            if user == bot:
                print('Wygrałeś')
                game_nr += 1
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


def main():
    print(f'Witaj w grze cieppło - zimno\n')
    max_games = input('Podaj liczbę gier: ')
    while True:
        try:
            max_games = int(max_games)
            break
        except ValueError:
            max_games = input('POdaj wartość numeryczną liczby gier: ')
    cieplo_zimno(max_games)


main()