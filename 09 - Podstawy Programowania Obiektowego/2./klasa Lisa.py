from playsound import playsound


class Canis:
    paws = 4
    ears = 2
    tail = 1

    def __init__(self):
        print('Jestem wilkowaty')

    def show_description(self):
        print('''Species of this genus are distinguished
               by their moderate to large size, their massive,
               well-developed skulls and dentition,
               long legs, and comparatively short ears and tails''')


class Fox(Canis): ##lisy ndziedziczą z wilkowatych

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return "Lis istnieje"

    def show_description(self):
        super().show_description()
        print("""
                Lis jaki jest
                każdy widzi
                """)

    def WhatDoesTheFoxSay(self):
        #playsound('/USers/piotr/Downloads/3888.mp3')
        print("IT'S HIS VOICE")
## wykorzystano  https://voicebot.su/pl/sound/odglosy-lisa-w-oddali/
fox = Fox('Lisek ')

fox.WhatDoesTheFoxSay()
print(fox.tail)
fox.show_description()