def a(cislo):
    if cislo == 0:
        print(0)
    else:
        a(cislo - 1)
        print(cislo)

a(2)
