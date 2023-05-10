'''
def mood(name):
    print(f'How are you {name}')

x = input('What is your name? ')
mood(x)



def my_mood(answear):
    return answear * 2
resp = input('How are you? ')
twiced = my_mood(resp)
my_mood(resp)
print('My mood is like',twiced)
'''

def add_book(number):
    libary = {}
    for i in range(number):
        a = input('Podaj tytuł książki: ')
        b = input('Podaj rating książki: ')
        while True:
            try:
                b = int(b)
                break
            except ValueError:
                b = input('Podaj rating książki jako liczbę: ')
        libary[a] = b
    return libary

def book_number(data):
    a = input('Podaj numer książki: ')
    while True:
        try:
            a = int(a)
            break
        except ValueError:
            a = input('Numer to cyfra. Podaj numer książki: ')
    while True:
        try:
            title, review = shelf[a-1]
            print(f'Ksiazka pt "{title}" "ma ocene {review}')
            #print(shelf[a-1])
            break
        except IndexError:
            print('Książki nie ma w bazie')
            a = input('Podaj numer książki: ')
            while True:
                try:
                    a = int(a)
                    break
                except ValueError:
                    a = input('Numer to cyfra. Podaj numer książki: ')


counter = int(input('Ile książek dodajesz?: '))
data = add_book(counter)
print(data)
shelf = list(data.items())
book_number(shelf)

