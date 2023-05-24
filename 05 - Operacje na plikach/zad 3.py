import random
from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw()
file = askopenfilename(filetypes=[("Pliki tekstowe", "*.txt")])


def quotes(file):
    with open(file,'r') as file:
        lines = file.readlines()
    return lines

def choose_linse(lines):
    chosen = quotes(file)
    return print(chosen[0:5])

a = quotes(file)
choose_linse(a)