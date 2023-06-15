import random as ran
class Player:

    def blast(self, enemy):
        print("Pif paf - strzela Bohatery")
        damage = ran.randint(1, 10)
        print("Damage: ", damage)
        if damage > 3:
            enemy.die()
        else:
            print("No i spudłowałem, stwierdził Bohater")
            enemy.win()
class Alien:

    def die(self):
        print('Obcy z trudem łapie oddech, "To już koniec. Ale prawdziwie wielki koniec... \n',
              'Walczyliśmy do końca. Nie, to nie koniec. Larwy moje jednoczcie się! \n',
              'O tak one pomszczą mnie pewnego dnia... \n',
              'Żegnaj, okrutny Wszechświecie! Umieeeraaam"')

    def win(self):
        print('Obcy mlaska i zjada przeciwnika ze smakiem')


if __name__ == '__main__':
    print('************ Śmierć Obcego ************\n')

    hero = Player()
    invader = Alien()
    hero.blast(invader)
    input('\n\nAby zakończyć program, naciśnij klawisz Enter.')


hero = Player()
invader = Alien()