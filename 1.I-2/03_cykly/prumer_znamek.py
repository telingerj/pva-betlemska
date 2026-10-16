# uživatel zadá počet známek, pak zadává každou známku
# úkolem je spočítat průměr z těchto zadaných čísel

pocet_znamek = int(input("zadej počet známek: "))
soucet = 0
i = 0
while i < pocet_znamek:
    aktualni_znamka = int(input("zadej " + str(i + 1) + ". známku: "))
    soucet += aktualni_znamka
    i += 1

print("tvůj průměr je", soucet / pocet_znamek)
