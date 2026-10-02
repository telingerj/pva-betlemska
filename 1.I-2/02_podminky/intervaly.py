#  A = (0;10)
#  B = <5;6>
#  C = (2;4) u (6;10)
#  D = <6;10> u <11;15>

cislo = float(input())

# rozhodnout, do kterých intervalů číslo patří

if cislo > 0 and cislo < 10:
    print("A")

if cislo >= 5 and cislo <= 6:
    print("B")

if (cislo > 2 and cislo < 4) or (cislo > 6 and cislo < 10):
    print("C")

if (cislo >= 6 and cislo <= 10) or (cislo >= 11 and cislo <= 15):
    print("D")
