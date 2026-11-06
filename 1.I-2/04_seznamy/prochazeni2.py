#TODO: vytvořit program, který spočítá, kloikrát je v seznamu Filip
jmena = ["Milan", "Anna", "Jan", "Filip", "Martina", "Filip", "Eliška", "Filip"]

pocet = 0
for i in range(len(jmena)):
    if jmena[i] == "Filip":
        pocet += 1

print("počet Filipů je", pocet)
