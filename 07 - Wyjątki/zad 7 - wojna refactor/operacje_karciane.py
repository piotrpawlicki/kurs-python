import random

import operacje_graczy as og
GAME_RANGE = ['B','b','G','g']
def Talia_kart():
    figury = {'AS': 12, 'KRÓL': 11, 'DAMA': 10, 'WALET': 9, '10': 8, '9': 7, '8': 6,'7': 5,'6': 4, '5':3, '4': 2, '3': 1, '2': 0}
    kolory = ['KARO', 'KIER', 'PIK', 'TREFL']
    talia = {}

    for kolor in kolory:
        for figura, wartosc in figury.items():
            figura_n = figura + ' ' + kolor
            wartosc_n = wartosc
            talia[figura_n] = wartosc_n
    return talia


def Przypisz_Karty(talia):
    gracz = {}
    gracz_temp = []
    bot = {}
    bot_temp = []
    talia_temp = list(talia.keys())
    random.shuffle(talia_temp)
    for i in range(0,10):
        gracz_temp.append(talia_temp[i])
    for i in gracz_temp:
        if i in talia:
            gracz[i] = talia[i]
    for i in range(11,21):
        bot_temp.append(talia_temp[i])
    for i in bot_temp:
        if i in talia:
            bot[i] = talia[i]
    return gracz, bot


def sortuj_talie(talia):
    a = dict(sorted(talia.items(), key=lambda x: x[1], reverse=True))
    return a


def wartosc_karty(karta, talia):
    if karta in talia:
        val = talia[karta]
        return val
    else:
        return None

def znajdz_klucz(slownik, wartosc):
    for klucz, wart in slownik.items():
        if wart == wartosc:
            return klucz
    return None


def porownaj_karty(moc_gracza, moc_bota):
    if moc_gracza > moc_bota:
        return 'Gracz wygrał'
    elif moc_bota> moc_gracza:
        return 'Bot wygrał'

def usun_karte(talia, karta):
    for key in karta.keys():
        del talia[key]
    return talia

def dodaj_karte(karta_przeciwnika, talia):
    talia.update(karta_przeciwnika)
