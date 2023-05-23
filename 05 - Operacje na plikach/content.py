PLIK = '/Users/piotr/Desktop/Python/kurs-python/0000 PLIKI/pan_tateusz.txt'

# with open(PLIK) as fopen:
#     #for line in fopen:
#     #    print(line)
#     while True:
#         current_line = fopen.readline()
#         if current_line == '':
#             break
#         print(current_line)

def czytaj_plik(PLIK):
    with open(PLIK) as fopen:
        content_list = fopen.read()
    return content_list

def wyswietl(lista):
        print(lista)

def main():
    a = czytaj_plik(PLIK)
    print(wyswietl(a))

main()