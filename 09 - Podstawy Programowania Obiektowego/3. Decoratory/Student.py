import holidays
class Student:
    university = 'UAM'
    min_avg = 4.5

    def __init__(self, name, last, age, student_avg):
        self.name = name
        self.last = last
        self.age = age

    def __str__(self):
        return self.name.capitalize() + " " + self.last.capitalize()


    @property
    def email(self):
        return f'{self.last.lower()}.{self.name[0].lower()}@uam.com'
    @property
    def fullname(self):
        return f' {self.last} {self.name}'
    @fullname.setter
    def fullname(self, name):
        self.last, self.name  = name.split()

    #
    # def grand_scholarship(self):
    #     if self.student_avg >= self.min_avg:
    #         print('Przyznano stypendium')
    #     else:
    #         print('Odmowa przyznania stypendium')
    #
    # @classmethod
    # def set_min_avg(cls, new_min_avg):
    #     cls.min_avg = new_min_avg
    #
    # @staticmethod
    # def is_academic_day(day):
    #     if day.weekday() == 5 or day.weekday() == 6 or day in holidays.PL() :
    #         return False
    #     else:
    #         return True