import random
from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw()
file = askopenfilename(filetypes=[("Pliki tekstowe", "*.txt")])


def quotes(file):
    with open(file,'r') as file:
        lines = file.readlines()
        chosen = random.sample(lines,3)
        return chosen


chosen = quotes(file)
for i in chosen:
    to_split = i.split(' - ')
    for elem in to_split:
        print(elem)