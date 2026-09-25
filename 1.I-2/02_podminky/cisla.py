cislo = int(input("cislo: "))

#  zjistit, jestli je číslo jednomístné, dvoumístné nebo třímístné
#  zjistit, na jakou číslici číslo končí

if cislo <= 9:
    print("číslo je jednomístné")
elif cislo <= 99:  # je potřeba použít elif, aby program nevypsal že je číslo jednomístné a dvoumístné zároveň
    print("číslo je dvoumístné")
elif cislo <= 999:
    print("číslo je třímístné")

print("číslo končí na číslici", cislo % 10)  # modulo - zbytek po dělení 10
print("předposlední číslice je", (cislo % 100) // 10)  # bonus
