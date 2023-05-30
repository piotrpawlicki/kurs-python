import random
import operacje_karciane as ok
def wybor_gracza(gracz_talia):
    gracz_talia_disp = list(ok.sortuj_talie(gracz_talia))
    print(gracz_talia_disp)
    karta_gracza = input(f'\nWybierz kartę z talii: ').upper()

    while karta_gracza not in gracz_talia:
        print(f'Nie masz takiej karty\n')
        karta_gracza = input(f'\nWybierz kartę z talii: ').upper()
    moc_gracza = ok.wartosc_karty(karta_gracza, gracz_talia)
    return {karta_gracza : moc_gracza}

##wybor bota dla gry gdy bot zaczyna
def wybor_bota_bot_pierwszy(talia_bota):
    losowa_karta = random.choice(list(talia_bota.keys()))
    losowa_moc = talia_bota[losowa_karta]
    karta_bota = {losowa_karta : losowa_moc}
    return karta_bota

def wybor_bota_bot_drugi(karta_gracza,talia_gracza, talia_bota):
        moc_bota = 0
        #moc_gracza = wartosc_karty(karta_gracza, talia_gracza)
        moc_gracza = list(karta_gracza.values())[0]
        if moc_gracza >= max(talia_bota.values()):
            moc_bota = min(talia_bota.values())
        ##elif moc_gracza == max(talia_bota.values()):
          ##  print('remis')
        else:
            ##znajdź ta karty które są większe, posortuj i wywal najmniejszą
            for elem in talia_bota.values():
                if elem > moc_gracza:
                    if elem < moc_bota or moc_bota ==0:
                        moc_bota = elem #moc_bota to klucz
        karta_bota = ok.znajdz_klucz(talia_bota,moc_bota)
        return {karta_bota: moc_bota}
