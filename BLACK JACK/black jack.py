import gry as g, karty as k


class BJ_Card(k.Card):
    """Klasa reprezentująca kartę na stole."""
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v


class BJ_Deck(k.Deck):
    """Klasa reprezentująca talia kart do gry."""

    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))


class BJ_Hand(k.Hand):
    """ Reka w black jacku """

    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super().__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
            return rep
        else:
            return "None"

    @property
    # jesli Twoja karta ma wartoś None tp suma wartosci też None
    def total(self):
        for card in self.cards:
            if not card.value:
                return None

        # sumuj asa jako 1
        t = 0
        for card in self.cards:
            t += card.value
        ##czy zawiera asa
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True
        # jesli zawiera asa, a suma jest mniejsza od 11 to dodaj 1 do sumy
        if contains_ace and t <= 11:
            t += 10
        return t

    def is_busted(self):
        return self.total > 21


class BJ_Player(BJ_Hand):
    def is_hitting(self):
        response = g.ask_yes_no("\n" + self.name + ", chcesz dobrać kartę? (T/N): ")
        return response == "t"

    def bust(self):
        print(self.name, "ma furę.")
        self.lose()

    def lose(self):
        print(self.name, "przegrywa.")

    def win(self):
        print(self.name, "wygrywa.")

    def push(self):
        print(self.name, "remisuje.")


class BJ_Dealer(BJ_Hand):
    """ Rozdający w blackjacku. """

    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "ma furę.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BJ_Game(object):
    """ Gra w blackjacka. """

    def __init__(self, names):
        self.players = []

        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Rozdający")
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()


    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp


    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()



    def play(self):
        # rozdaj każdemu początkowe dwie karty
        self.deck.deal(self.players + [self.dealer], per_hand=2)
        self.dealer.flip_first_card()  # ukryj pierwszą kartę rozdającego
        for player in self.players:
            print(player)
        print(self.dealer)

        # rozdaj graczom dodatkowe karty
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()  # odsłoń pierwszą kartę rozdającego

        if not self.still_playing:
            # ponieważ wszyscy gracze dostali furę, pokaż tylko rękę rozdającego
            print(self.dealer)
        else:
            # daj dodatkowe karty rozdającemu
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                # wygrywa każdy, kto jeszcze pozostaje w grze
                for player in self.still_playing:
                    player.win()
            else:
                # porównaj punkty każdego gracza pozostającego w grze z punktami rozdającego
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        # usuń karty wszystkich graczy
        for player in self.players:
            player.clear()

        # usuń karty rozdającego
        self.dealer.clear()


def main():
    print("\t\tWitaj w grze 'Blackjack'!\n")
    names = []
    number = g.ask_number("Podaj liczbę graczy (1 - 7): ", low=1, high=8)

    for i in range(number):
        name = input("Wprowadź nazwę gracza: ")
        names.append(name)
    print()

    game = BJ_Game(names)

    again = None
    while again != "n":
        game.play()
        again = g.ask_yes_no("\nCzy chcesz zagrać ponownie?: ")


if __name__ == '__main__':
    main()
    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
