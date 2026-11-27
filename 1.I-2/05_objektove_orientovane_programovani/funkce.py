hodnota = 1

def pozdrav():  # funkce - má nějaký kód a kdykoliv ji můžeme zavolat (i víckrát) a tím spustit její kód
    print("ahoj, já jsem funkce")

def druha_mocnina(x):  # hodnota x je parametr - při volání tam uložíme nějakou hodnotu
    return x * x  # return = hodnota, která je výstupem funkce

def maximum(cislo1, cislo2):  # dva parametry
    if cislo1 > cislo2:
        return cislo1  # jakmile funkce narazí na return, okamžitě končí
    return cislo2

def cislo_na_text(cislo):
    cisla = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    return cisla[cislo]

def globalni_promenna():
    global hodnota  # chceme pracovat s globální proměnnou
    hodnota = 2
    print("změnil jsem hodnotu na", hodnota)

print(druha_mocnina(2))
cislo = druha_mocnina(10)
print(cislo)
print(maximum(10, 15))
print(maximum(2, 1))
text = "Na SPŠS Betlémská je " + cislo_na_text(5) + " tříd v ročníku a " + cislo_na_text(4) + " ročníky"
print(text)
globalni_promenna()
print(hodnota)