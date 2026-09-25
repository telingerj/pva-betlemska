x = int(input())
y = int(input())
z = int(input())

# vypsat čísla podle pořadí

# 1. možnost
if x > y and x > z:
    print(x, end=" ")
    if y < z:
        print(z, end=" ")
        print(y, end=" ")
    else:
        print(y, end=" ")
        print(z, end=" ")

if y > z and y > x:
    print(y, end=" ")
    if x < z:
        print(z, end=" ")
        print(x, end=" ")
    else:
        print(x, end=" ")
        print(z, end=" ")

if z > x and z > y:
    print(z, end=" ")
    if x < y:
        print(y, end=" ")
        print(x, end=" ")
    else:
        print(x, end=" ")
        print(y, end=" ")
print()

# 2. možnost

if x > y > z:
    print(x, y, z)
elif x > z > y:
    print(x, z, y)
elif y > x > z:
    print(y, x, z)
elif y > z > x:
    print(y, z, x)
elif z > x > y:
    print(z, x, y)
elif z > y > x:
    print(z, y, x)
