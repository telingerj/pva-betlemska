tajna_zprava = "poklad je zakopany na ostrove pod stromem"
zasifrovana_zprava = ""
posnun = 3

#TODO: nešifrovat mezery - zachovat je v zašifrované zprávě tak, jak jsou

for i in range(len(tajna_zprava)):
    pismeno = tajna_zprava[i]
    if pismeno == " ":
        zasifrovana_zprava += " "
    else:
        pismeno_kod = ord(pismeno)
        pismeno_kod += posnun
        zasifrovana_zprava += chr(pismeno_kod)

print(zasifrovana_zprava)
