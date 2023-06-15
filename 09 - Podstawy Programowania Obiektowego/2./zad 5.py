from abc import ABC, abstractmethod

class Pojazdy(ABC):

    def __init__(self, marka, kolor):
        self.nazwa = marka
        self.kolor = kolor
    @abstractmethod
    def jedz(self):
        pass
    @abstractmethod
    def hamuj(self):
        pass
    @abstractmethod
    def prawo_jazdy(self):
        pass

class Samochod(Pojazdy):

    def jedz(self):
        print("Jade")
    def hamuj(self):
        print("Hamuje")
    def prawo_jazdy(self):
        print("Prawo jazdy : B")

class Motocykl(Pojazdy):

        def jedz(self):
            print("Jade")
        def hamuj(self):
            print("Hamuje")
        def prawo_jazdy(self):
            print("Prawo jazdy : A")

class Autobus(Pojazdy):

    def jedz(self):
        print("Jade")
    def hamuj(self):
        print("Hamuje")
    def prawo_jazdy(self):
        print("Prawo jazdy : D")


moto = Motocykl("Moto", "Czerwony")

print(moto.nazwa)