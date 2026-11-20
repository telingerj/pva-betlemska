tajna_zprava = "ecmttd lt ncshpccm pi hsvgcxm iof hhtwfeo"
heslo = "pocitac"
heslo_i = 0
zasifrovana_zprava = ""

rozsifrovat = True

for i in range(len(tajna_zprava)):
    pismeno = tajna_zprava[i]
    if pismeno == " ":
        zasifrovana_zprava += " "
    else:
        pismeno_heslo = heslo[heslo_i]
        heslo_i += 1
        if heslo_i == len(heslo):
            heslo_i = 0
        posun = ord(pismeno_heslo) - ord("a")
        if rozsifrovat:
            posun = -posun
        kod = ord(pismeno)
        kod += posun
        if kod > ord("z"):
            kod -= 26
        if kod < ord("a"):
            kod += 26
        zasifrovana_zprava += chr(kod)
        #TODO: zařídit, aby se pismeno posunulo o tolik, kolikáté je v abecedě pismeno_heslo
        # a => 0, b => 1 ...
print(zasifrovana_zprava)
