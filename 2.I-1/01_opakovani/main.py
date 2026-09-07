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

vstup = input("zadej vstup: ")

print("první znak:", vstup[0])
print("poslední znak:", vstup[len(vstup) - 1])






















# soubory
# vytvořit soubor 0.txt, zapsat do něj vstup od uživatele
# vytvořit soubor 1.txt, který bude obsahovat počet znaků v souboru 0.txt


# OOP
# třída člověk obsahující jméno, příjmení, datum narození
# třída auto obsahující značku, rok výroby, barvu, nájezd, řidiče a majitele

# majitel auta může přepsat auto na někoho jiného
# majitel auta může autu přidat řidiče
# řidič může s autem ujet nějakou vzdálenost, přičte se do nájezdu
