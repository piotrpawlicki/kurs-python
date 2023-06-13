class Mammals:
    head = 1
    eyes = 2

    def show_description(self):
        return "Ssak jaki jest każdy widzi"

class Cat(Mammals):
    def __init__(self, name):
        self.name = name

class Human(Mammals):
    def __init__(self, name):
        self.name = name

    def describe(self):
        super().show_description()
        print('Człowiek - wszystko jasne')

mela = Cat('Mela')
czlowiek = Human('Jan')
print(mela.eyes)

print(czlowiek.head)

czlowiek.describe()