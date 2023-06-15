def ask_yes_no(question):
    """Zadaj pytanie, na które można odpowiedzieć tak lub nie."""
    response = None
    while True:
        response = input(question).lower()
        if response == "y" or response == "n":
            return response
        else:
            print("I have no clue what that means. Try again! ")

def ask_number(question, low, high):
    """Poproś o podanie liczby z określonego zakresu."""
    response = None
    while True:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print("Value error! Try again.")
        if response < low or response > high:
            print("Number is out of range.")
        else:
            break


if __name__ == "__main__":
    print("Uruchomiłeś ten moduł bezpośrednio (zamiast go zaimportować).")
    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")