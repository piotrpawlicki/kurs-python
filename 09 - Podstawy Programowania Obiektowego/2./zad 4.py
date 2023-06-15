import datetime as dt
import pytz

class Clock:
    def __init__(self):
        self.time = dt.datetime.now(tz=pytz.timezone('Europe/Warsaw'))

    def show_time(self):
        print(self.time)

    def time_zone(self):
        print(self.time.tzinfo)

class Calendar:
    def __init__(self):
        self.date = dt.date.today()

    def show_date(self):
        print(self.date)

    def show_whole_month(self):
        year = self.date.year
        month = self.date.month
        date = dt.date(year, month, 1)
        month_name = date.strftime("%B")
        print(f"Miesiąc: {month_name} {year}")
        print("Pon  Wt  Śr Czw Pt Sob Ndz")

        # Określanie dnia tygodnia pierwszego dnia miesiąca
        first_day_weekday = date.weekday()

        # Wypełnianie spacjami przed pierwszym dniem miesiąca
        print("    " * first_day_weekday, end="")

        # Wyświetlanie dni miesiąca
        while date.month == month:
            print(f"{date.day:2d}", end="  ")
            if date.weekday() == 6:
                print()
            date += dt.timedelta(days=1)

        print()

class ClockCalendar(Clock, Calendar):
    def __init__(self):
        Clock.__init__(self)
        Calendar.__init__(self)


my_clock = ClockCalendar()
my_clock.time_zone()
my_clock.show_whole_month()