import random
import operacje_graczy as og
import operacje_karciane as ok
GAME_RANGE = ['B','b','G','g']

def start_gry():
    x = input('Kto zaczyna grę Gracz (G) czy Bot (B)? : ')
    while x not in GAME_RANGE:
        x = input('Zły input! Kto zaczyna grę Gracz (G) czy Bot (B)? : ')
    return x


def main():
    talia = ok.Talia_kart() #talia jest słownikiem
    gracz_talia, bot_talia = (ok.Przypisz_Karty(talia))  #karty bota i gracza to również słowniki - tasowanie kart i ich rozdanie
    start = start_gry().upper()
    wynik_gracza = 0
    wynik_bota = 0
    if start == 'G':
        while len(gracz_talia) > 0 and len(bot_talia) > 0:
            gracz_karta = og.wybor_gracza(gracz_talia)
            print(f'Gracz wybrał kartę {gracz_karta}')
            bot_karta = og.wybor_bota_bot_drugi(gracz_karta, gracz_talia, bot_talia )
            print(f'Bot wybrał kartę {bot_karta}')

            moc_gracza = list(gracz_karta.values())[0] ##wartosc_karty(gracz_karta, talia)
            moc_bota = list(bot_karta.values())[0]
            wynik = ok.porownaj_karty(moc_gracza, moc_bota)
            print(wynik)
            ##
            if wynik == 'Gracz wygrał' :
                wynik_gracza +=1
                ok.usun_karte(gracz_talia,gracz_karta)
                ok.usun_karte(bot_talia, bot_karta)
                ##usun_karte(list(bot_karta.keys())[0], bot_talia)
            elif wynik == 'Bot wygrał':
                wynik_bota += 1
                ok.usun_karte(gracz_talia, gracz_karta)
                ok.usun_karte(bot_talia, bot_karta)

    else:
        while len(gracz_talia) > 0 and len(bot_talia) > 0:
            bot_karta = og.wybor_bota_bot_pierwszy(bot_talia)
            print(f'Bot wybrał kartę {bot_karta}')
            gracz_karta = og.wybor_gracza(gracz_talia)
            print(f'Gracz wybrał kartę {gracz_karta}')
            moc_gracza = list(gracz_karta.values())[0]
            moc_bota = list(bot_karta.values())[0]
            wynik = ok.porownaj_karty(moc_gracza, moc_bota)
            print(wynik)
            if wynik == 'Gracz wygrał':
                wynik_gracza += 1
                ok.usun_karte(gracz_talia, gracz_karta)
                ok.usun_karte(bot_talia, bot_karta)
                ##usun_karte(list(bot_karta.keys())[0], bot_talia)
            elif wynik == 'Bot wygrał':
                wynik_bota += 1
                ok.usun_karte(gracz_talia, gracz_karta)
                ok.usun_karte(bot_talia, bot_karta)

    if wynik_bota > wynik_gracza:
        print('Wojnę wygrał bot')
    elif wynik_gracza > wynik_bota:
        print('Wojnę wygrał gracz')
    else:
        print('padł remis')


if __name__ == '__main__':
    main()








