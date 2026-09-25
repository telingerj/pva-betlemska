def swap(l, a, b):
    temp = l[a]
    l[a] = l[b]
    l[b] = temp


def is_sorted(l):
    for i in range(0, len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True


def bubble_sort1(l):
    for j in range(0, len(l)):  # = opakuj
        for i in range(0, len(l) - 1):
            if l[i] > l[i + 1]:
                swap(l, i, i + 1)


def bubble_sort2(l):
    for j in range(0, len(l)):  # = opakuj
        for i in range(0, len(l) - 1 - j):
            if l[i] > l[i + 1]:
                swap(l, i, i + 1)
