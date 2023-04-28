########################################################################################
# Zad1
print('***********************************')
print('Zad1\n\n')

table=['buty', 'plecak', 'termos', 'czapka']
table = sorted(table, key=str.lower)
print(table)

########################################################################################
# Zad2
print('***********************************')
print('Zad2\n\n')

counter = 0
user_ans = []
user_ans_fin = []
while counter < 10:
    x = int(input('Wprowadź liczbę: '))
    user_ans.append(x)
    counter += 1

for i in user_ans:
    if i % 2 == 0:
        user_ans_fin.append(i)
print(user_ans_fin)

########################################################################################
# Zad3
print('***********************************')
print('Zad3\n\n')

counter = 0
user_ans = []
user_ans_fin = []

while counter < 4:
    while True:
        x = input('Wprowadź liczbę: ')
        try:
            x = int(x)
            break
        except ValueError:
            print('Nie wprowadziłeś liczby! Wprowadź liczbę: ')

    user_ans.append(x)
    counter += 1
first = user_ans[0]
last = user_ans[(len(user_ans) - 1)]
if first == last:
    print('Pierwszy i ostatni są takie same')
else:
    print('Pierwszy i ostatni są inne')


########################################################################################
# Zad4
print('***********************************')
print('Zad4\n\n')

counter = 0
user_ans = []
user_ans_fin = []
while counter < 4:
    x = (input('Wprowadź wartość: '))
    user_ans.append(x)
    counter += 1
middle_1 = user_ans[int(len(user_ans)/2)]
middle_2 = user_ans[int((len(user_ans)/2 ) -1)]

if middle_1 == middle_2:
    print('Oba środkowe są takie same')
else:
    print('Oba środkowe są inne')

########################################################################################
# Zad5
print('***********************************')
print('Zad5\n\n')

ppl = [
['Dorota', 'Wellman', 'dziennikarka']
,['Adam', 'Małysz', 'sportowiec']
,['Robert','Lewandowski', 'piłkarz']
,['Krystyna', 'Janda', 'aktorka']
]

for i in ppl:
    person = ' '.join(i)
    person = person[:person.rfind(' ')] + '-' + person[person.rfind(' ')+1:]
    print(person)


########################################################################################
# Zad5
print('***********************************')
print('Zad5\n\n')

ppl = [
['Dorota', 'Wellman', 'dziennikarka']
,['Adam', 'Małysz', 'sportowiec']
,['Robert','Lewandowski', 'piłkarz']
,['Krystyna', 'Janda', 'aktorka']
]

for row in ppl:
    for id, elem in enumerate(row):
        if id == int(len(row)-2) :
            print(elem, end = "-")
        else:
            print(elem, end = ' ')
    print()