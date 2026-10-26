def binary_search(l, val):
    binary_search_rec(l, val, 0, len(l) - 1)

def binary_search_rec(l, val, left, right):
    mid = (left + right) // 2
    if val > l[mid]:
        print("číslo je v pravé půlce")
    elif val < l[mid]:
        print("číslo je v levé půlce")
    else:
        print("číslo je na pozici", mid)


l = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007]
val = 1001
binary_search(l, val)
