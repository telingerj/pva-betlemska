#  rozhodne, kolik má kvadratická rovnice řešení
#  vyřeší ji
#  ax^2 + bx + c = 0
a = int(input())
b = int(input())
c = int(input())

D = b ** 2 - 4 * a * c
if D > 0:
    D = D ** 0.5
    x1 = (-b + D) / (2 * a)
    x2 = (-b - D) / (2 * a)
    print("rovnice má tyhle dvě řešení:", x1, x2)
if D < 0:
    print("rovnice nemá řešení")
if D == 0:
    x = -b / (2 * a)
    print("rovnice má tohle jedno řešení:", x)
