print('***********************************')
print('Zad4\n\n')

tab_mn = [[i * j for j in range(1, 11)] for i in range(1, 11)]

for row in tab_mn:
    for num in row:
        print("{:4d}".format(num), end="")
    print()