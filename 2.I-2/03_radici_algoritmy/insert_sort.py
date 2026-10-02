def swap(l, a, b):
    temp = l[a]
    l[a] = l[b]
    l[b] = temp

def insert_sort(l):
    for i in range(1, len(l)):
        j = i
        while j > 0 and l[j] < l[j - 1]:
            swap(l, j, j - 1)
            j -= 1
