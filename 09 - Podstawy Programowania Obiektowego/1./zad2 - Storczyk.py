import datetime as dt

class Orchid:
    kingdom = 'Plantae'

    def __init__(self, color, flowering_time, species):
        self.color = color
        self.flowering_time = dt.datetime.strptime(flowering_time, '%d-%m-%Y').date()
        self.species = species

    def flower_time(self):
        if self.flowering_time == dt.date.today():
            return "Flowering time is now!"
        elif self.flowering_time < dt.date.today():
            return "It's already gone"
        else:
            return "Be patient, flowering is coming"

orchid1 = Orchid('white', '01-01-2024', 'Storczyk pospolity')
print(orchid1.flower_time())