cislo = int(input())  # uživatel zadá buď 0 nebo 1

if cislo == 0:
    cislo = 1  # prohození 0 za 1
elif cislo == 1:  # elif-em zaručíme, že se budeme ptát jen když předchozí podmínka neprošla
    cislo = 0  # prohození 1 za 0

print(cislo)
