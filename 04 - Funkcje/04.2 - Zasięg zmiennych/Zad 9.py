import datetime


def check_type(value):
    while True:
        try:
            value = int(value)
            break
        except ValueError:
            value = input('Błąd typu! Podaj wartość jeszcze raz: ')
    return value


def get_car_details():
    brand = input('Podaj markę: ')
    model = input('Podaj model: ')
    year_of_prod = check_type(input('Podaj rok produkcji: '))
    is_original = check_type(input('Podaj procent oryginalnych części: '))
    detais = dict(brand=brand, model=model, year_of_prod=year_of_prod, is_original=is_original)
    return detais


def is_car_historical(details):
    current_year = int(datetime.datetime.now().year)
    age = current_year - int(details['year_of_prod'])
    original = int(details['is_original'])
    return True if age >= 25 and original >= 75 else False


def car_status(details):
    user_brand = details['brand']
    user_model = details['model']
    user_original = details['is_original']
    if is_car_historical(details):
        print(f'Gratulacje! Twój samochód {user_brand} {user_model} może być zarejestrowany jako zabytek')
    else:
        print(
            f'Twój samochód {user_brand} {user_model} jest za młody, albo ma za mało originalnych części (tylko {user_original} %)')


def main():
    user_car = get_car_details()
    print(user_car)
    car_status(user_car)


main()
