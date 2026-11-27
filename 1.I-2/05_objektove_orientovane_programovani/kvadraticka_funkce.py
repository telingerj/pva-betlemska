def diskriminant(a, b, c):
    return (b ** 2) - (4 * a * c)

def pocet_reseni(d):
    if d == 0:
        return 1
    if d < 0:
        return 0
    return 2

def vyresit(a, b, c):
    d = diskriminant(a, b, c)
    if pocet_reseni(d) == 0:
        return []
    elif pocet_reseni(d) == 1:
        return [-b / (2 * a)]
    return [(-b + d ** 0.5) / 2*a, (-b - d ** 0.5) / 2*a]

print(vyresit(1, 0, 0))
print(vyresit(1, 0, -4))
print(vyresit(1, 2, 1))
print(pocet_reseni(diskriminant(1, 2, 1)))
print(diskriminant(1, 2, 1))
print(pocet_reseni(5))