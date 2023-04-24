##Zad1
print('***********************************')
print('ZAD 1')
age = input("Enter your age: ")
print('Your age in binary is: ', bin(int(age)))

########################################################################################

##Zad2
print('***********************************')
print('ZAD 2')
bin_num = 1001111
bin_num = str(bin_num)

str_len = len(bin_num)
str_len = str_len - 1

a0 = 2^0 * int(bin_num[str_len])
a1 = 2^1 * int(bin_num[str_len-1])
a2 = 2^2 * int(bin_num[str_len-2])
a3 = 2^3 * int(bin_num[str_len-3])
a4 = 2^4 * int(bin_num[str_len-4])
a5 = 2^5 * int(bin_num[str_len-5])
a6 = 2^6 * int(bin_num[str_len-6])

conv_bin_num = a0 + a1 + a2 + a3 + a4 + a5 + a6
print(conv_bin_num)

########################################################################################
## Zad2 druga opcja
print('***********************************')
print('ZAD 2 - druga opcja')
bin_num = input("Enter binary number: ")

# Sprawdzenie poprawności formatu
while bin_num.isdigit() == False:
    print("Wrong format!")
    bin_num = input("Enter binary number: ")

dec_num = 0               ## inicjacja zmiennej dec_num
power = len(bin_num) - 1  ## wyliczenie maksymalnej potęgi

for digit in bin_num:     ## nie definiuję wcześniej zmiennej digit, bo to zmienna tymczasowa dla pętli for
    dec_num = dec_num + int(digit) * (2 ** power)
    power = power - 1
print("Decimal value:", dec_num)

########################################################################################
##Zad3
print('***********************************')
print('ZAD 3')
hex_num = 0x1DB
oct_num = 0o2063

print(hex_num)
print(oct_num)
