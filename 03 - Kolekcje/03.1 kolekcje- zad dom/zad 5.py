print('***********************************')
print('Zad5\n\n')

poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

poem = poem.lower().replace(",", "").split()
poem_count = {}

for word in poem:
    if word not in poem_count:
        poem_count[word] = 1
    else:
        poem_count[word] += 1
print("{:4d}".format(poem_count), end="")

for a,b in poem_count.items():
    print(f'{a} - {b}')