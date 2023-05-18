import random

GUESSING_WORDS = (
    "adam",
    "bank",
    "czar",
    "dama",
    "elita",
    "fanka",
    "grosz",
    "hobby",
    "idea",
    "jacht",
    "kawa",
    "lampa",
    "mama",
    "niska",
    "okno",
    "panda",
    "rabat",
    "samba",
    "tango",
    "ulica",
    "veto",
    "warta",
    "xerox",
    "yacht",
    "zakop",
    "balkon",
    "czas",
    "dywan",
    "ekran",
    "futro",
    "garaz",
    "haslo",
    "ilustracja",
    "jablko",
    "kanapa",
    "latarka",
    "maska",
    "niedzwiedz",
    "okulary",
    "pilot",
    "rakietka",
    "siekiera",
    "traktor",
    "uniform",
    "wazon",
    "xylofon",
    "yeti",
    "zamek",
    "konik",
    "lampa"
)

##konwersja słowa na listę
def create_list(word):
    return list(word)

##konwersja wybranego słowa na podkreślenia
def convert_word(word):
    a = list('X' * len(word))
    return a

##wyświetlanie prawidłowe
def display(word_list):
    return ' '.join(word_list)

##wybór słowa z listy słów
def select_word(word_list):
    a = len(word_list)
    b =  random.randint(0 , a-1)
    result = word_list[b]
    return result

## user input
def user_input():
    a = input("Podaj literę: ")
    while len(a) == 1 and a.isalpha():
        return a.upper()
    else:
        print("Błąd wejścia, podaj literę.")

##sprawdzenie czy litera jest w słowie
def check_input(UserInput, word_list):
    indexes = []
    for i in range(len(word_list)):
        if word_list[i] == UserInput:
            indexes.append(i)
    return indexes


##podmienienie znaku w liście
def change_char(guess_list, indeks, user_input):
    guess_list[indeks] = user_input

def check_results(list1, list2):
    if list1 == list2:
        return True
    else:
        return False

def hangman(number):
    hangman = [
        '''
           +---+
               |
               |
               |
               |
               |
        =======''',
        '''
           +---+
           |   |
               |
               |
               |
               |
        =======''',
        '''
           +---+
           |   |
           O   |
               |
               |
               |
        =======''',
        '''
           +---+
           |   |
           O   |
           |   |
               |
               |
        =======''',
        '''
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =======''',
        '''
           +---+
           |   |
           O   |
          /|\  |
               |
               |
        =======''',
        '''
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
        =======''',
        '''
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        ======='''
    ]

    return hangman[number]


def main():
    guess_number = 0
    guess_word = select_word(GUESSING_WORDS).upper()
    guess_word_list = create_list(guess_word)
    hidden_word_list = convert_word(guess_word)

    while not check_results(guess_word_list, hidden_word_list):
        print(hangman(guess_number))
        if guess_number == 7:
            break
        else:
            user_char = user_input()
            result = check_input(user_char, guess_word_list)
            if result:
                for i in result:
                    change_char(hidden_word_list, i , user_char)
            else:
                print('Spróbuj jeszcze raz')
                guess_number += 1
                print(f'guess number = {guess_number}')
        print(display(hidden_word_list))

    if check_results(guess_word_list, hidden_word_list):
        print('Gratuluję, wygrałeś!')
    else:
        print('Wisisz, koleżko.')

main()