print('***********************************')
print('Zad4\n\n')

tab = [[i*j for j in range(1,11)] for i in range(1,11)]

for row in tab:
    for elem in row:
        print(elem, end='\t')
    print()
