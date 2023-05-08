txt = input('Enter txt for encrypt: ')
while True:
    offset = input('Enter offset value: ')
    try:
        offset = int(offset)
        break
    except ValueError:
        print('Value error! Enter value: ')
txt_encrypted = ''
for char in txt:
    if ord(char) + offset > 127:
        offsetted_char = chr(ord(char) + offset - 127)
        txt_encrypted += offsetted_char
    elif ord(char) == 32:
        offsetted_char = ' '
        txt_encrypted += offsetted_char
    else:
        offsetted_char = chr(ord(char)+offset)
        txt_encrypted += offsetted_char
print(txt_encrypted)