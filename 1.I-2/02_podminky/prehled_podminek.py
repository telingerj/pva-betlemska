cislo = int(input())

if cislo > 10:  # větší než
    print("podmínka 1 je splněna")

if cislo < 10:  # menší než
    print("podmínka 2 je splněna")

if cislo >= 10:  # větší nebo rovno
    print("podmínka 3 je splněna")

if cislo <= 10:  # menší nebo rovno
    print("podmínka 4 je splněna")

if cislo == 5:  # rovnost - pozor! - je potřeba použít dvě rovná se ==
    print("podmínka 5 je splněna")

if cislo != 5:  # nerovnost
    print("podmínka 6 je splněna")

if ((cislo + 2) * 5) > 100:  # aritmetické operace v podmínce - můžeme použít, je potřeba používat závorky
    print("podmínka 7 je splněna")
