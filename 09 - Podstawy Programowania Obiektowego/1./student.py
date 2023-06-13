class Student:
    school = 'UAM'
    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age = age

    def email(self):
        return (f'{self.lastname}.{self.firstname[0]}@{self.school}.pl').lower()

    def sound(self, number):
        return f' go {self.school}! ' * number

    def __str__(self):
        email = self.email()
        return f'imie: {self.firstname}; nazwisko : {self.lastname}, wiek : {self.age}, email: {email}'

anna = Student('Anna','Nowak',23)
adam = Student('Adam','Snow',22)
#adam = Student()
anna.lastname = 'kowal'

print(adam)
# anna.name = 'Anna'
# adam.name = 'Adam'
# anna.age = 23
# adam.name = 31
#
# print(anna.name)
# print(anna.age)
