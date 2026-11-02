def binary_search(l, val):
    return binary_search_rec(l, val, 0, len(l) - 1)

def binary_search_rec(l, val, left, right):
    mid = (left + right) // 2
    if left > right:
        return -1
    elif left == right:
        if l[left] == val:
            return left
        return -1


    if val > l[mid]:
        return binary_search_rec(l, val, mid + 1, right)  # hledané číslo je v pravé půlce
    elif val < l[mid]:
        return binary_search_rec(l, val, left, mid - 1)  # hledané číslo je v levé půlce
    else:
        return mid


l = [2, 3, 4, 6, 7, 8, 9]
val = 10
print(binary_search(l, val))
