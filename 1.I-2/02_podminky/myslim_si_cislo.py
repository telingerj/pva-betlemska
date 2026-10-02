#  zeptáme se uživatele na jeho odhad
#  odpovíme, jestli je číslo větší / menší / rovné

cislo = 21  # číslo, které se uživatel snaží uhádnout
odhad = int(input())  # uživatelův odhad

if odhad == cislo:
    print("trefil jsi se!")
elif odhad > cislo:
    print("tvoje číslo moc velké!")
elif odhad < cislo:
    print("tvoje číslo je moc malé")
