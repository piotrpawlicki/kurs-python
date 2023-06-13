class Mammals:
    head = 1
    eyes = 2

    # def __str__(self):
    #     return "Ssak jaki jest każdy widzi"

class Cat(Mammals):
    def __init__(self,name):
        self.name = name

class Human(Mammals):
    def __init__(self, name):
        self.name = name

Mela = Cat
ja = Human
print(Mela.eyes)
print(ja.head)