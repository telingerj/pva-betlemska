x = 1
y = 1

while y <= 20:
    x = 1
    while x <= 20:
        if x * y < 10:
            print("  ", end="")  # zarovnání - jednomístná čísla před sebou musí mít dvě mezery (...) aby zabíraly stejně místa jako třímístná
        elif x * y < 100:
            print(" ", end="") # (...) a dvoumístná jednu
        print(x * y, end=" ")
        x += 1
    y += 1
    print()
