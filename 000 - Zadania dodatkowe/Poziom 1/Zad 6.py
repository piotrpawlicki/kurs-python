txt = input('Insert text: ')

txt_slicing = txt[::-1]
print(f' with string slicing : {txt_slicing}')
print('*************************')

txt_for = ''
for a in range(len(txt)-1, -1, -1):
    txt_for +=txt[a]
print(f' with for: {txt_for}')

print('*************************')

txt_while = ''
txt_len = len(txt)-1
while txt_len >= 0:
    txt_while += txt[txt_len]
    txt_len -= 1
print(f' with while: {txt_while}')