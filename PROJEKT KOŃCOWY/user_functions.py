from getpass import *
import tkinter as tk
import sys
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


def ask_number2(question):
    """Poproś o podanie liczby z określonego zakresu."""
    response = None
    while True:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print("Value error! Try again.")


def ask_for_password():
    """Poproś o podanie hasła."""
    password = ""
    counter = 0
    while counter < 3:
        counter += 1
        password = getpass(prompt = "Password: ") #getpass(prompt = "Password: ")
        if password == "password":
            return True
        else:
            counter += 1
            password = getpass(prompt = "Password: ")

    print("Too many attempts. Goodbye.")
    return False


def ask_string(window, prompt):
    result = tk.StringVar()
    label = tk.Label(window, text=prompt)
    label.pack()
    entry = tk.Entry(window, textvariable=result)
    entry.pack()

    def close_window():
        window.destroy()

    button = tk.Button(window, text="OK", command=close_window)
    button.pack()

    window.mainloop()
    return result.get()