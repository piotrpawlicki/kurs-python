# dom = 0
# szkola = 1
# kosciol = 2
# bar = 3
# szpital = 4
# kino = 5
# teatr = 6
wierzcholki = ['dom','szkola','kosciol','bar','szpital','kino','teatr']

macierz=[
[0,1,1,1,0,0,0],
[1,0,0,0,1,0,0],
[1,0,0,1,0,1,0],
[1,0,1,0,1,0,0],
[0,1,0,1,0,1,1],
[0,0,1,0,1,0,1],
[0,0,0,0,1,1,0],
]

def main():
    for row in macierz:
        i=0
        while i < len(row):
            if row[i] == 1:
                print(f'{wierzcholki[macierz.index(row)]} -> {wierzcholki[i]}')
            i += 1

if __name__ == '__main__':
    main()
