VELIKOST = 7  # konstanta = nikde v programu se její hodnota nemění

#TODO: vytvořit čtverec z hvězdiček, který má délku strany VELIKOST

# čtverec
"""
for y in range(VELIKOST):
    for x in range(VELIKOST):
        print("*", end="")
    print()
"""

# pravoúhlý trojúhelník vlevo
"""
for y in range(VELIKOST):
    for x in range(y + 1):
        print("*", end="")
    print()
"""
# pravoúhlý trojúhelník vpravo
"""
for y in range(VELIKOST):
    for x in range(VELIKOST - (y + 1)):
        print(" ", end="")
    for x in range(y + 1):
        print("*", end="")
    print()
"""

# rovnostranný trojúhelník
"""
pocet_radku = VELIKOST // 2 + 1
for y in range(pocet_radku):
    pocet_hvezdicek = 2*y + 1
    pocet_mezer = pocet_radku - (y + 1)
    for x in range(pocet_mezer):
        print(" ", end="")
    for x in range(pocet_hvezdicek):
        print("*", end="")
    print()
"""

for x in range(VELIKOST):
    print("*", end="")
print()

for y in range(VELIKOST - 2):
    print("*", end="")
    for x in range(VELIKOST - 2):
        print(" ", end="")
    print("*")

for x in range(VELIKOST):
    print("*", end="")
print()

#  *****
#  *   *
#  *   *
#  *   *
#  *****
