# proměnné, datové typy
# zeptat se uživatele na hodnotu a vypsat, jestli se jedná o celé číslo, desetinné číslo nebo řetězec
# celé číslo vynásobit dvěma, desetinné číslo zaokrouhlit na celé a pro řetězec vypsat jeho délku
"""
a = input("zadej hodnotu: ")
try:  # v bloku try vyzkoušíme spustit daný kód
    a = int(a)
    print("dvojnásobek čísla je", a * 2)
except:  # pokud by kód vyhodil chybu, spustí se místo toho kód v bloku except
    try:
        a = float(a)
        print("zaokrouhlené číslo je", round(a))
    except:
        print("délka řetězce je", len(a))
"""

# cykly
# ptát se na číslo tak dlouho, dokud uživatel nezadá "konec"
# vypsat součet všech těchto čísel

# vypsat čísla od 1 do 100
#  - běžně
#  - pozpátku
#  - pouze sudá čísla

"""
vstup = ""
soucet = 0
while True:  # ptáme se pořád dokola
    vstup = input("zadej číslo: ")
    try:  # zkusíme převést vstup na číslo
        vstup = int(vstup)
    except:  # když se to nepovede, přestaneme se ptát (vyskočíme z while cyklu pomocí break)
        break
    soucet += vstup  # přičteme číslo do součtu
print("součet je:", soucet)
"""

"""
for i in range(100):
    print(i)

for i in range(100, 0, -1):
    print(i)

for i in range(2, 100, 2):
    print(i)
"""


# seznamy (řetězce)
# zeptat se na textový řetězec, vypsat
#  - první znak
#  - poslední znak
#  - vypsat řetězec pozpátku
#  - zjistit, jestli je řetězec palindrom (slovo, které se píše stejně zepředu i zezadu)

"""
retezec = input("zadej text: ")
print("první znak:", retezec[0])
print("poslední znak:", retezec[-1])
prevraceny_retezec = ""
for i in range(len(retezec) - 1, -1, -1):
    prevraceny_retezec += retezec[i]
print("převrácený řetězec:", prevraceny_retezec)
if retezec == prevraceny_retezec:
    print("text je palindrom")
else:
    print("text není palindrom")
"""

# soubory
# vytvořit soubor 0.txt, zapsat do něj vstup od uživatele
# vytvořit soubor 1.txt, který bude obsahovat počet znaků v souboru 0.txt


# OOP
# třída člověk obsahující jméno, příjmení, datum narození
# třída auto obsahující značku, rok výroby, barvu, nájezd, řidiče a majitele

# majitel auta může přepsat auto na někoho jiného
# majitel auta může autu přidat řidiče
# řidič může s autem ujet nějakou vzdálenost, přičte se do nájezdu
