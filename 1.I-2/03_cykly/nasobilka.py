x = 1
y = 1

while y <= 10:
    x = 1  # po každém skončení vnitřního cyklu vyresetujeme hodnotu jeho řídící proměnné (v tomto případě x)
    while x <= 10:  # vnitřní cyklus - násobení x s každým jednotlivým y
        print(x, "*", y, "=", x * y)
        x += 1
    y += 1
