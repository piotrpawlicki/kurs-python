from tkinter import Tk
from tkinter.filedialog import askopenfilename


def open_file():
    try:
        Tk().withdraw()
        filename = askopenfilename()
        with open(filename, 'r') as fopen:
            if fopen == '':
                return print('Empty file')
            return fopen.read()
    # Work with your open file
    except FileExistsError:
        print('File does not exist')

def safe_save_file(filename, data):
    try:
        with open(filename, 'x') as fopen:
            fopen.write(data)
    except FileExistsError:
        print('File cannot be overwritten')