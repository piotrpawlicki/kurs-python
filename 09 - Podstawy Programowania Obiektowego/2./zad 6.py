class Country:

    def __init__(self,area, population, capital, currency, language):
        self.area = area
        self.population = population
        self.capital = capital
        self.currency = currency
        self.language = language


    def __str__(self):
        return f'Country: {self.area}\n Population: {self.population}\n Caplital {self.capital} \n Currency{self.currency}\n Language {self.language}'

Germany = Country(area=357022, population=81802257, capital='Berlin', currency='Euro', language='German')
Poland = Country(area=312685, population=38652600, capital='Warsaw', currency='Polish', language='Polish')
France = Country(area=592, population=65705000, capital='Paris', currency='Euro', language='French')
Italy = Country(area=301, population=60427000, capital='Rome', currency='Euro', language='Italian')

coiuntries = [Germany, Poland, France, Italy]

for country in coiuntries:
    print(f'{country}\n')