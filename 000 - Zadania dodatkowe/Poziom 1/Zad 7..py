a = [3, 6, 12, 54, 21, 35, 2, 9]
max_num_a = a[0]
for i in range(1,len(a)):
    if max_num_a < a[i]:
        max_num_a = a[i]
print(f'{max_num_a} = max from a \n')

b = [9, 0, 30, 25, 44, 71, 42, 5, 17, 89, 39, 10, 22, 1]

max_num_b = b[0]
for i in range(1, len(a)):
    if max_num_b < b[i]:
        max_num_b = b[i]

print(f'{max_num_b} = max from b\n')
