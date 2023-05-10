########################################################################################
# Zad1
print('***********************************')
print('Zad1\n\n')

list_to_dicts = [['a', 'b'],['c', 'd'],['e', 'f']]
dict_from_list = dict(list_to_dicts)
print(dict_from_list)

########################################################################################
# Zad2
print('***********************************')
print('Zad2\n\n')

tuple_to_dics = (('a', 'b'),('c', 'd'),('e', 'f'))
dict_from_tuple = dict(tuple_to_dics)
print(dict_from_tuple)

########################################################################################
# Zad3
print('***********************************')
print('Zad3\n\n')

n = input('Input number: ')
while True:
    try:
        n = int(n)
        break
    except ValueError:
        n = input('Value error!, Input number: ')

char = input('Input 1 char: ')

tab = [str(char) * n] * n

for row in tab:
    print(' '.join(row))

########################################################################################
# Zad4
print('***********************************')
print('Zad4\n\n')

tab_mn = [[i * j for j in range(1, 11)] for i in range(1, 11)]

for row in tab_mn:
    for num in row:
        print("{:4d}".format(num), end="")
    print()

########################################################################################
# Zad5
print('***********************************')
print('Zad5\n\n')

poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

poem = poem.lower().replace(",", "").split()
poem_count = {}
szybko = 0
zbudz = 0
for word in poem:
    if word not in poem_count:
        poem_count[word] = 1
    else:
        poem_count[word] += 1
print("{:4d}".format(poem_count), end="")

for a,b in poem_count.items():
    print(f'{a} - {b}')

########################################################################################
# Zad6
print('***********************************')
print('Zad6\n\n')

days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}
days_set = set(days.values())
days_list = list(days_set)
print(days_list)

########################################################################################
# Zad7
print('***********************************')
print('Zad7\n\n')

example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
example_tuple = tuple(set(example_list))
max_elem = max(example_tuple)
min_elem = min(example_tuple)
print(f'min elem : {min_elem}\nmax_elem : {max_elem}')
