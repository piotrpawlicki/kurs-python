class Pen:
    def __init__(self, width):
        self.width = width

    def show_description(self):
        print('Pen')

class Pineapple:
    def __init__(self, color):
        self.color = color

    def show_description(self):
        print('Pineapple')

class PenPineapple(Pen, Pineapple):
    def __init__(self, width, color):
        super().__init__(width)
        Pineapple.__init__(self, color)

    def show_description(self):
        super().show_description()
        Pineapple.show_description(self)

sth = PenPineapple('red', 10)
sth.show_description()