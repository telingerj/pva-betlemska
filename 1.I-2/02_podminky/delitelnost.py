# program, který se zeptá na číslo a zjistí, jestli je sudé (dělitelné dvěma)

cislo = int(input())

if cislo % 2 == 0:
    print("číslo je sudé")
else:
    print("číslo je liché")


# zjistit, kterými čísly od 2 do 10 je číslo dělitelné
print("je dělitelné těmito čísly: ", end="")
if cislo % 2 == 0:
    print("2 ", end="")
if cislo % 3 == 0:
    print("3 ", end="")
if cislo % 4 == 0:
    print("4 ", end="")
if cislo % 5 == 0:
    print("5 ", end="")
if cislo % 6 == 0:
    print("6 ", end="")
if cislo % 7 == 0:
    print("7 ", end="")
if cislo % 8 == 0:
    print("8 ", end="")
if cislo % 9 == 0:
    print("9 ", end="")
if cislo % 10 == 0:
    print("10 ", end="")

# BONUS: zjistit, jestli je číslo dělitelné 3 a zároveň 7 - bez použití and, or, pomocí jedné podmínky
