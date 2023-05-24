import random
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
file = askopenfilename(filetypes=[("Pliki tekstowe", "*.txt")])

def get_text(file):
    with open(file,'r') as file:
        txt = file.read()
        return txt

def devide_list(txt):
    txt = txt.replace(',','').split()
    return txt

longest_word = ''
txt = get_text(file)
txt = devide_list(txt)

for i in txt:
    if len(longest_word) < len(i):
        print()
        longest_word = i

print(f'{longest_word} : len = {len(longest_word)}')



