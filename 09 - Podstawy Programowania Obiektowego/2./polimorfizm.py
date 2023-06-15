class Horse:
    def poop(self):
        print('poop')


class Unicorn:
    def poop(self):
        print("Magic rainbow")

def test(animal):
    animal.poop()

def main():
    arrow = Horse()
    cute = Unicorn()

    test(arrow)
    test(cute)


main()