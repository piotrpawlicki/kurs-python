import random
from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw()
file = askopenfilename(filetypes=[("Pliki tekstowe", "*.txt")])

def quotes(file):
    with open(file,'r') as file:
        for line in file:
            quote = file.readlines()
            chosen = random.choice(quote)
            width = len(chosen)
            print('Quote of the day is: ')
            print('*'* width)
            to_split = chosen.split(' - ')
            for elem in to_split:
                print(elem.strip().center(width))
            print('*'* width)

quotes(file)