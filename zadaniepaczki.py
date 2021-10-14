minimalna_waga_elementu = 1
maksymalna_waga_elementu = 10
maksymalna_waga_paczki = 20
numer_paczki = 1
wyslane_kilogramy = 0
aktualna_waga = 0
waga_najlzejszej_paczki = 20
numer_najlzejszej_paczki = 0
maksymalna_liczba_elementow = int(input("Podaj maksymalna liczbe elementow: "))



for idx in range(maksymalna_liczba_elementow):
    waga_elementu = int(input("Podaj wage elementu: "))
    if waga_elementu == 0:
        print("Blad - waga elementu nie moze wynosic 0")
        break
    elif waga_elementu < minimalna_waga_elementu or waga_elementu > maksymalna_waga_elementu:
        print("Waga elementu nie miesci sie w dozwolonym zakresie")
        break
    else:
        wyslane_kilogramy += waga_elementu
        if aktualna_waga + waga_elementu <= maksymalna_waga_paczki:
            aktualna_waga += waga_elementu
        else:
            numer_paczki += 1

            if aktualna_waga < waga_najlzejszej_paczki:
                waga_najlzejszej_paczki = aktualna_waga
                numer_najlzejszej_paczki = numer_paczki
        aktualna_waga = waga_elementu

if maksymalna_liczba_elementow == 0:
    print("Liczba paczek to 0")

else:
    numer_paczki += 1

    if aktualna_waga < waga_najlzejszej_paczki:
        waga_najlzejszej_paczki = aktualna_waga
        numer_najlzejszej_paczki = numer_paczki

    puste_kilogramy = numer_paczki * 20 - wyslane_kilogramy
    puste_kilogramy_najlzejsza = 20 - waga_najlzejszej_paczki

    print("Liczba wyslanych paczek to: {}. Liczba wyslanych kilogramow to {}. Suma pustych kilogramow to: {}. "
              "Najlzejsza paczka jest paczka o numerze {}. Sa w niej {} puste kilogramy."
              .format(numer_paczki, wyslane_kilogramy, puste_kilogramy, numer_najlzejszej_paczki, puste_kilogramy_najlzejsza))