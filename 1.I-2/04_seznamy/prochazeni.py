jmena = ["Milan", "Anna", "Jan", "Martina", "Eliška", "Filip"]

# je v seznamu Filip?

nalezeno = False
pozice = 0
for i in range(len(jmena)):  # procházíme všechny indexy v seznamu
    if jmena[i] == "Filip":  # a pro každý kontrolujeme, jestli tam není Filip
        nalezeno = True
        pozice = i
        break  # vyskočí ven z for cyklu

if nalezeno:
    print("je tam Filip a je na pozici", pozice)
else:
    print("není tam Filip")
