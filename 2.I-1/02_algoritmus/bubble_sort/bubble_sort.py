from prace_se_seznamy import swap

def bubble_sort1(l):
    for j in range(len(l) - 1):
        for i in range(0, len(l) - 1):
            if l[i] > l[i + 1]:
                swap(l, i, i + 1)


def bubble_sort2(l):
    for j in range(len(l) - 1):
        for i in range(0, len(l) - j - 1):
            if l[i] > l[i + 1]:
                swap(l, i, i + 1)
