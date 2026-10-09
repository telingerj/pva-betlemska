# vypsat čísla od 2 do 100, která jsou dělitelná 4, ale ne 3
a = 2
while a <= 100:
    if a % 4 == 0 and a % 3 != 0:
        print(a)
    a += 1
