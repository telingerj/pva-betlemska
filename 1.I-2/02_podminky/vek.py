vek = int(input("zadej věk: "))

if vek >= 18:  # podmínka - ptáme se na otázku...
    print("jsi dospělý")  # a pokud je to pravda, provedeme odsazený kód
elif vek >= 15:  # elif - v případě, že nebyla splněna předchozí podmínka, ptáme se na další
    print("jsi mladistvý")
else:  # else - provedeme, pokud nebyla splněna žádná z předchozích podmínek
    print("jsi dítě")

print("děkuji za použití mého programu!")  # tento řádek se provede vždy (nezávisle na podmínkách)
