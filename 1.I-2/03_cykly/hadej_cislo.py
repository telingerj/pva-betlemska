tajne_cislo = 23
uzivatel_cislo = 0
pocet_pokusu = 0

while tajne_cislo != uzivatel_cislo:  # opakujeme dokud číslo není uhádnuto
    pocet_pokusu += 1
    uzivatel_cislo = int(input("Tvůj tip: "))
    if uzivatel_cislo > tajne_cislo:
        print("Tohle číslo je moc velké! Zadej menší!")
    elif uzivatel_cislo < tajne_cislo:
        print("Tohle číslo je moc malé! Zadej větší!")
    else:
        print("Gratuluji! Uhádl jsi mé číslo!")
        print("potřeboval jsi k tomu", pocet_pokusu, "pokusů")
