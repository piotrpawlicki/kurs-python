import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw()
file = askopenfilename(filetypes=[("Pliki tekstowe", "*.txt")])

file_size = os.path.getsize(file)
print(file_size)