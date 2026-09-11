jmeno = input("zadej jméno: ")  # příkaz input slouží k načtení vstupu od uživatele, vstup se uloží do proměnné s názvem jmeno
print("ahoj uživateli", jmeno)  # vypisujeme pozdrav s uživatelovým jménem na obrazovku

vek = int(input("zadej věk: "))  # když se vstupem nrchceme pracovat jako s textem, ale jako s číslem, je potřeba input obalit funkcí int
print("za", 18 - vek, "let budeš plnoletý")  # pomocí 18 - vek spočítáme počet let, které uživateli zbývají do plnoletosti
