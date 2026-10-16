num = 3210

def binary_search(l):
    ...
    left = 0
    right = len(l) - 1
    mid = (left + right) // 2
    if l[mid] > num:
        print("číslo je v levé půlce")
    elif l[mid] < num:
        print("číslo je v pravé půlce")
    else:
        print("číslo jsem našel")

l = [5, 10, 15, 20, 21, 26, 30]
binary_search(l)