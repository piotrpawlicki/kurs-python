

## zadanie 1 od Kuby
'''
distance = 120
gas_price = 5.04
consumption = 6.4

fin_price = distance * (consumption / 100) * gas_price
print('Price is: ', fin_price, 'PLN')
'''
## zadanie rozbudowane

distance = int(input('Enter lenght of your trip: '))         ## wprowadzenie długości wyprawy
gas_price = int(input('Enter gas price: '))                  ## wprowadzenie ceny paliwa
consumption = int(input('Enter combustion per 100km: '))     ## wprowadzenie spalania na 100 km

fin_price = distance * (consumption / 100) * gas_price
print('Price is: ', fin_price, 'PLN')
