cislo1 = int(input())
cislo2 = int(input())

if cislo1 == 1 and cislo2 == 1:  # and - a zároveň - zkoumáme jestli platí obě podmínky najednou
    print("podmínka 1 je splněna")

if cislo1 == 1 or cislo2 == 1:  # or - nebo - zkoumáme jestli platí aspoň jedna podmínka (klidně můžou platit obě najednou)
    print("podmínka 2 je splněna")

if not cislo1 > 10:  # not - negace - zkoumáme jestli podmínka NENÍ splněna
    print("podmínka 3 je splněna")

if (cislo1 < 5 and cislo2 < 5) or (cislo1 > 10 and cislo2 > 10):
    print("podmínka 4 je splněna")
