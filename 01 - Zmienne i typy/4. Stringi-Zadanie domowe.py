## zad1
print('***********************************')
print('ZAD 1')
word = 'abcdefghi'
len_word = len(word)

val = int((len_word - 3) / 2)
print(word[val: -val])
########################################################################################
## zad2
print('***********************************')
print('ZAD 2')
s1 = 'abcd'
s2 = 'SZKLANKA'

val = (len(s1)/2)
val = int(val)
s3 = s1[:val]+ s2 + s1[val:len(s1)]
print(s3)
########################################################################################
## zad3

print('***********************************')
print('ZAD 3')
quote = 'Honesty is the first chapter in the book of wisdom.'

len_quote = len(quote)
print('len_quote : ', len_quote)     ##Policz wszystkie znaki w napisie

index_start = quote.find('wisdom')   ##Nie modyfikując zmiennej wyświetl słowo wisdom
wisdom_len=len('wisdom')
index_stop = wisdom_len + index_start
print(quote[index_start:index_stop])


index_start = quote.find('.')        ##Wyświetl tylko kropkę
dot_len=len('.')
index_stop = dot_len + index_start
print(quote[index_start:index_stop])

print(quote[:int(len_quote/2)])      ##Wyświetl tylko pierwszą połowę tekstu

quote_new=quote.replace(' ','')      ##Wyświetl od połowy tylko co trzecią literę cytatu
len_quote_new = len(quote_new)
print(quote_new[int(len_quote_new / 2)::3])

print(quote[::2])                    ##Wyświetl ‘Hnsyi h is hpe ntebo fwso.’

##Wyświetl cały cytat odwrotnie
txt = quote
lenght = len(txt)
lenght = -lenght
txt_rev = ''
i = - 1
while i >= lenght:
    txt_rev = txt_rev + txt[i]
    i = i - 1
print(txt_rev)

##Zamień wisdom na słowo friendship
replaced = quote.replace('wisdom','friendship')
print(replaced)
########################################################################################

## zad4

print('***********************************')
print('ZAD 4')
title = input('Insert book title: ')
title_new = title.replace(' ','')
while title_new.isalpha() == False:
    title = input('Wrong format! Insert book title: ')
    title_new = title.replace(' ', '')

name = input('Insert author name: ')
name_new = name.replace(' ','')
while name_new.isalpha() == False:
    name = input('Wrong format! Insert author name: ')
    name_new = name.replace(' ', '')

pages = input('Insert number of pages: ')
while pages.isnumeric() == False:
    pages = input('Wrong format! Insert number of pages: ')

title = title.lower()
title = title.capitalize()

name = name.lower()
name = name.capitalize()

book = title + ' ' + name + ' ' + str(pages)
print(book)
print('len(book)= ',len(book))


########################################################################################

## zad5
print('***********************************')
print('ZAD 5')
txt = input('Insert text: ')
len_txt=int(len(txt)/2)

if len(txt) > 2:
    if len_txt %2 == 1:
        half1 = txt[:len_txt]
        half2 = txt[len_txt + 1:]
    else:
        half1 = txt[:len_txt]
        half2 = txt[len_txt:]
    ##reverse half2
    if len(half2) > 1:
        i = -1
        rev_half2 = ''
        while i >= -len_txt:
            rev_half2 = rev_half2 + half2[i]
            i = i - 1
    elif len(half2) == 1:
        rev_half2 = half2
elif len(txt) == 2:
    half1 = txt[0]
    half2 = txt[1]
    rev_half2 = half2

elif len(txt) ==1:
    half1 = txt[0]
    half2 = txt[0]
    rev_half2 = half2
half1 = half1.upper()
rev_half2 = rev_half2.upper()
if half1 == rev_half2:
    print('Your text is the palindrome')
else:
    print('Your text is not the palindrome')

########################################################################################

##zad5 wersja 2
print('***********************************')
print('ZAD 5 - second version')
txt = 'Kobyła ma mały bok'
txt = txt.upper()
txt = txt.replace(' ','')
txt2 = txt[::-1]
print(txt==txt2)

########################################################################################

## zad6
print('***********************************')
print('ZAD 6')
import this
##dekodowanie this zgodnie ze wzorem z this.py
txt  = "".join([this.d.get(c, c) for c in this.s])

## liczenie better
better_count = txt.split().count('better')
print('Number of better: ',better_count)

## Usuń z tekstu symbol gwiazdki

txt_2 = txt.replace('*','')
print('This without * : ', txt_2)

##Zamień jedno wystąpienie explain na understand

txt_explain = txt.replace('explain','understand',1)
print(txt_explain)

##usuń spacje i połącz wszystkie słowa myślnikiem
txt_space_removed = txt.replace(" ","-")
print(txt_space_removed)

##Podziel tekst na osobne zdania za pomocą kropki

txt_split = txt.split('.')
print(txt_split)


########################################################################################
## zad7
print('***********************************')
print('ZAD 7')
number = 1234
word = 'blablabla'
print('In one sentence i can use number: {} and word: {}'.format(number,word))


