import datetime

##jeśli auto ma min 25 lat wyświetl komunikat Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”

def get_car_details():
    brand = input('Podaj markę: ')
    model = input('Podaj model: ')
    year_of_prod = input('Podaj rok produkcji: ')
    while True:
        try:
            year_of_prod = int(year_of_prod)
            break
        except ValueError:
            year_of_prod = input('Podaj rok produkcji (jako numer): ')
    detais = {'brand': brand, 'model' : model, 'year_of_prod' : year_of_prod}
    return detais

def is_car_historical(details):
    current_year = int(datetime.datetime.now().year)
    age = current_year - int(details['year_of_prod'])
    return True if age >= 25 else False

def car_status(details):
    user_brand = details['brand']
    user_model = details['model']
    if is_car_historical(details):
        print(f'Gratulacje! Twój samochód {user_brand} {user_model} może być zarejestrowany jako zabytek')
    else:
        print(f'Twój samochód {user_brand} {user_model} jest za młody')

user_car = get_car_details()
print(user_car)
car_status(user_car)