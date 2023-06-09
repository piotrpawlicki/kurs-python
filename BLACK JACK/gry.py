# gry.py
# Demonstruje tworzenie modułu

class Player(object):
    """ Uczestnik gry. """
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep

    def is_busted(self):
        return self.total > 21

def ask_yes_no(question):
    """Zadaj pytanie, na które można odpowiedzieć tak lub nie."""
    response = None
    while True:
        response = input(question).lower()
        if response == "t" or response == "n":
            return response
        else:
            print("Nie wiem o co chodzi.")

def ask_number(question, low, high):
    """Poproś o podanie liczby z określonego zakresu."""
    response = None
    while True:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print("Wprowadzona wartość nie jest liczbą.")
        else:
            if response < low or response > high:
                print("Wprowadzona wartość jest spoza zakresu.")
            else:
                break


if __name__ == "__main__":
    print("Uruchomiłeś ten moduł bezpośrednio (zamiast go zaimportować).")
    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")