txt = input('Enter txt for decrypt: ')
while True:
    offset = input('Enter offset value: ')
    try:
        offset = int(offset)
        break
    except ValueError:
        print('Value error! Enter value: ')
txt_decrypted = ''
for char in txt:
    if ord(char) - offset < 127:
        offsetted_char = chr(ord(char) - offset + 127)
        txt_decrypted += offsetted_char
    elif ord(char) == 32: ## wyjątek na brak deskrypcji spacji
        offsetted_char = ' '
        txt_decrypted += offsetted_char
    else:
        offsetted_char = chr(ord(char) - offset)
        txt_decrypted += offsetted_char
print(txt_decrypted)