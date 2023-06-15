import holidays
import datetime as dt

from django.urls import path


class Student:
    university = 'New York Academy'
    min_avg = 4.45

    def __init__(self, name, last, age, student_avg):
        self.name = name
        self.last = last
        self.age = age
        self.student_avg = student_avg

    def __str__(self):
        return self.name.capitalize() + " " + self.last.capitalize()

    def email(self):
        return f'{self.last}.{self.name[0]}.university.com'

    def get_scholarship(self):
        if self.student_avg >= self.min_avg:
            print('Przyznano')
        else:
            print('Nie przyznano')

    @classmethod
    def set_min_avg(cls, new_min_avg):
        cls.min_avg = new_min_avg

    @staticmethod
    def academic_day(day):
        if day.weekday() == 5 or day.weekday() == 6 or day in holidays.PL():
            return False
        else:
            return True

today = dt.date(2021, 1, 6) ##dt.datetime.today()
print(today)
Student.academic_day(today)
print(Student.academic_day(today))


