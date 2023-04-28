########################################################################################
# Zad1
print('***********************************')
print('Zad1\n\n')

krotka = (1,2,3,3)
krotka_w_set=set(krotka)
print(krotka_w_set)

########################################################################################
# Zad2
print('***********************************')
print('Zad2\n\n')
L_test = [1, 2, 3, 4]
T_test = (1, 2, 3, 4)
S_test = {1, 2, 3, 4}

print('Krotki i sety są kolekcjami niemodyfikowalnymi, dlatego nie posiadają takich metod jak append(), extend(), insert(), remove() czy pop(). Sety również nie posiadają metody sort(), ponieważ elementy w secie są nieuporządkowane.')
########################################################################################
# Zad3
print('***********************************')
print('Zad3\n\n')

k1 = (1,2,3,4)
k2 = (3,4,5,6)
k3 = []

for i in k1:
    if i % 2 == 1:
        k3.append(i)
for i in k2:
    if i % 2 == 0:
        k3.append(i)
k3 = set(k3)
print(k3)

########################################################################################
# Zad4
print('***********************************')
print('Zad4\n\n')

krotka =  [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
len_krotka = len(krotka)/3
lista1 = krotka[0:int(len_krotka)]
lista2 = krotka[int(len_krotka):2*int(len_krotka)]
lista3 = krotka[2*int(len_krotka):]
print(lista1)
print(lista2)
print(lista3)