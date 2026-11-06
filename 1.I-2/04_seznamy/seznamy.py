s = [4, 5, 9, 2, 0, 1]
print(s)  # vypíše celý seznam
print(s[0]) # vypíše číslo na indexu (pozici) 0 (pozor - čísluje se od 0, ne od 1)
print(s[2]) # vypíše číslo na indexu 2

s.append(3) # přidá na konec seznamu číslo 3
print(s)
s.pop(0)  # samže ze seznamu číslo na indexu 0
print(s)
s.pop()  # smaže ze seznamu poslední číslo
print(s)

s.remove(0)  # smaže číslo 0
print(s)

print(len(s))  # délka seznamu - počet prvků


"""
zak1 = "Jakub Novák"
zak2 = "Petr Novotný"
zak3 = "Anna Kovářová"
zak4 = "Eliška Potměšilová"

s = 0
if zak1 == "Jakub":
    s += 1
if zak2 == "Jakub":
    s += 1
if zak3 == "Jakub":
    s += 1
"""