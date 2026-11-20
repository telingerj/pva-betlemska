tajna_zprava = "srnodg mh cdnrsdqb qd rvwuryh srg vwurphp"
zasifrovana_zprava = ""
posnun = -3

for i in range(len(tajna_zprava)):
    pismeno = tajna_zprava[i]
    if pismeno == " ":
        zasifrovana_zprava += " "
    else:
        pismeno_kod = ord(pismeno)
        pismeno_kod += posnun
        if pismeno_kod > ord("z"):
            pismeno_kod -= 26
        elif pismeno_kod < ord("a"):
            pismeno_kod += 26
        zasifrovana_zprava += chr(pismeno_kod)

print(zasifrovana_zprava)
