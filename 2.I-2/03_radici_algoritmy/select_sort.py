def swap(l, a, b):
    temp = l[a]
    l[a] = l[b]
    l[b] = temp


def get_max_pos(l, start, end):
    max_pos = start
    for i in range(start, end + 1):
        if l[i] > l[max_pos]:
            max_pos = i
    return max_pos

def select_sort(l):
    for i in range(0, len(l) - 1):
        max_pos = get_max_pos(l, 0, len(l) - 1 - i)
        swap(l, max_pos, len(l) - 1 - i) #  chci aby na poslední pozici bylo největší číslo

