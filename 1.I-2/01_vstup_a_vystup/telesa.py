a = int(input("zadej délku hrany krychle: "))
print("objem krychle je", a ** 3)  # pomocí dvou hvězdiček umocníme číslo

r = int(input("zadej poloměr podstavy válce: "))
v = int(input("zadej výšku válce: "))
V_valec = 3.14 * r ** 2 * v  # vzoreček pro výpočet objemu válce
print("objem válce je", V_valec)

a2 = int(input("zadej délku strany podstavy jehlanu: "))
v2 = int(input("zadej výšku jehlanu: "))
V_jehlan = (a2 ** 2 * 2) / 3  # pomocí závorek můžeme upřednostnit některé operace před jinými (jako v matematice)
print("objem jehlanu je: ", V_jehlan)