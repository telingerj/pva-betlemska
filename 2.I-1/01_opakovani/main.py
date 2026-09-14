# proměnné, datové typy
# zeptat se uživatele na hodnotu a vypsat, jestli se jedná o celé číslo, desetinné číslo nebo řetězec
# celé číslo vynásobit dvěma, desetinné číslo zaokrouhlit na celé a pro řetězec vypsat jeho délku
# nápověda: použijte try - except

"""

vstup = input("zadej vstup: ")
try:
    vstup = int(vstup)
    print("dvojnásobek čísla:", vstup * 2)
except:
    try:
        vstup = float(vstup)
        print("zaokrouhlený vstup:", round(vstup))
    except:
        print(len(vstup))

"""

# cykly
# ptát se na číslo tak dlouho, dokud uživatel nezadá "konec"
# vypsat součet všech těchto čísel

"""
soucet = 0
while True:
    vstup = input("zadej číslo: ")
    if vstup == "konec":
        break
    vstup = int(vstup)
    soucet += vstup
print("součet čísel je:", soucet)
"""


# vypsat čísla od 1 do 100
#  - běžně
#  - pozpátku
#  - pouze sudá čísla

"""

for i in range(1, 101):
    print(i, end=" ")
print()

for i in range(100, 0, -1):
    print(i, end=" ")
print()

for i in range(2, 101, 2):
    print(i, end=" ")
print()

"""

# seznamy (řetězce)
# zeptat se na textový řetězec, vypsat
#  - první znak
#  - poslední znak
#  - vypsat řetězec pozpátku
#  - zjistit, jestli je text palindrom (text, který se píše stejně pozpátku jako běžně) (kobylamamalybok)

"""

vstup = input("zadej vstup: ")

print("první znak:", vstup[0])
print("poslední znak:", vstup[len(vstup) - 1])
pozpatku = ""
for i in range(len(vstup) - 1, -1, -1):
    pozpatku += vstup[i]
print(pozpatku)
if pozpatku == vstup:
    print("vstup je palindrom")
else:
    print("vstup není palindrom")
"""

# soubory
# vytvořit soubor 0.txt, zapsat do něj vstup od uživatele
# vytvořit soubor 1.txt, který bude obsahovat počet znaků v souboru 0.txt

"""
vstup = input("zadej vstup: ")

with open("0.txt", "w") as file:
    file.write(vstup)

with open("1.txt", "w") as file:
    file.write(str(len(vstup)))
"""


# OOP
# třída člověk obsahující jméno, příjmení, datum narození
# třída auto obsahující značku, rok výroby, barvu, nájezd, řidiče a majitele

# majitel auta může přepsat auto na někoho jiného
# majitel auta může autu přidat řidiče
# řidič může s autem ujet nějakou vzdálenost, přičte se do nájezdu


class Clovek:
    def __init__(self, jmeno, prijmeni, datum_narozeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.datum_narozeni = datum_narozeni


    def prepsat(self, auto, novy_majitel):
        if auto.majitel != self:
            return
        auto.majitel = novy_majitel


    def pridat_ridice(self, auto, ridic):
        if auto.majitel != self:
            return
        auto.ridic = ridic


    def jet(self, auto, vzdalenost):
        if auto.ridic != self:
            return
        auto.najezd += vzdalenost


class Auto:
    def __init__(self, znacka, rok_vyroby, barva, najezd, ridic, majitel):
        self.znacka = znacka
        self.rok_vyroby = rok_vyroby
        self.barva = barva
        self.najezd = najezd
        self.ridic = ridic
        self.majitel = majitel



c1 = Clovek("Franta", "Vomáčka", "1.9.1999")
c2 = Clovek("Janek", "Rubeš", "24.12.1987")

a1 = Auto("Škoda", "2005", "červená", 100540, c1, c1)
a2 = Auto("Volkswagen", "2012", "černá", 25412, c2, c2)


c1.prepsat(a1, c2)
print(a1.majitel.prijmeni)
c1.prepsat(a1, c1)
print(a1.majitel.prijmeni)
c2.prepsat(a1, c1)
print(a1.majitel.prijmeni)









