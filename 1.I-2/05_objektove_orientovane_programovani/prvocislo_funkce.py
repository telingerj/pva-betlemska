#TODO: vytvořit funkci, která umí rozhodnout, jestli je číslo prvočíslo
# funkce vrací True / False

def je_delitelne(a, b):
    return a % b == 0

def je_prvocislo(cislo):
    for i in range(2, cislo):
        if je_delitelne(cislo, i):
            return False
    return True

print(je_prvocislo(3))
print(je_prvocislo(5))
print(je_prvocislo(6))
print(je_prvocislo(22))
print(je_prvocislo(139))
