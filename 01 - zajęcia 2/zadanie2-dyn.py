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
