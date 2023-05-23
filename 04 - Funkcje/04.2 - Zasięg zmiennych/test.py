def user_input():
    while True:
        a = input("Podaj literę: ")
        try:
            len(a) == 1
            a.isalpha() == True
            break
        except ValueError:
           print('Błąd typu. Podaj literę')


a = user_input()
print(a)