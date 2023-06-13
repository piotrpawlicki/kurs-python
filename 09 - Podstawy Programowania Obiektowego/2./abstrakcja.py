from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def sides(self):
        pass
class Triangle(Shape):

    def __init__(self):
        print('Utworzono trójkąt')
    def sides(self):
        print("3 sides")


t = Triangle()
t.sides()