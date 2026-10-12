def swap(l, i, j):  # prohodí hodnoty v seznamu l na indexech i a j
    temp = l[i]
    l[i] = l[j]
    l[j] = temp
