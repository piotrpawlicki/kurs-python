##zad1

x='123'

if x.isdigit() == True:
    print('true')
else:
    print('false')

##zad2

txt = 'mata'
txt_center = txt.center(10,'*')
print(txt_center)

##zad3






##zad 6

txt = input('Insert text: ')
txt_len=len(txt)
i = 0
check = 0
if txt.isalnum() == True:
    while i < txt_len:
        if txt[i].isupper() == True:
            check = check + 1
            i = txt_len
        else:
           check = check
        i = i + 1
else:
    print('False')
if check > 0:
    print('True')
else:
    print('False')