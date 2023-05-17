subjects = []

for i in range (5):
    user_input = input('Podaj nazwy 4 przedmiotów szkolnych oddzielonych przecinkiem: ')
    subjects.extend(user_input.split(','))
    print(len(subjects))
    print(subjects)
    while len(subjects) != 4:
        user_input = input('Zła liczba przedmiotów. Podaj nazwy 4 przedmiotów szkolnych oddzielonych przecinkiem: ')



print('Wszystkie przedmioty szkolne to: ',','.join(subjects))
