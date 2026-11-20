#TODO: chceme udělat algoritmus, který určí k-tý největší prvek
# zkuste naprogramovat bez quicksortu

def swap(l, a, b):
    temp = l[a]
    l[a] = l[b]
    l[b] = temp

def find_biggest(l, k):
    l.sort()
    return l[len(l) - k]

def find_second_biggest(l):
    first_two = [l[0], l[1]]
    if first_two[0] < first_two[1]:
        swap(first_two, 0, 1)
    for i in range(2, len(l)):
        if l[i] > first_two[0]:
            first_two[1] = first_two[0]
            first_two[0] = l[i]
        elif l[i] > first_two[1]:
            first_two[1] = l[i]
    return first_two[1]


def quickselect(l, k):
    print(quickselect_rec(l, k, 0, len(l) - 1))

def quickselect_rec(l, k, left, right):
    if left == right:
        return l[left]
    pivot_index = left
    left_pointer = left + 1
    right_pointer = right
    while left_pointer < right_pointer:
        while left_pointer < right_pointer and l[left_pointer] <= l[pivot_index]:
            left_pointer += 1
        while left_pointer < right_pointer and l[right_pointer] > l[pivot_index]:
            right_pointer -= 1
        if left_pointer < right_pointer:
            swap(l, left_pointer, right_pointer)
    if l[left_pointer] <= l[pivot_index]:
        swap(l, left_pointer, pivot_index)
        pivot_index = left_pointer
    elif l[left_pointer] > l[pivot_index]:
        swap(l, left_pointer - 1, pivot_index)
        pivot_index = left_pointer - 1

    if pivot_index == len(l) - k:
        return l[pivot_index]
    if pivot_index > len(l) - k:
        return quickselect_rec(l, k, left, pivot_index - 1)
    if pivot_index < len(l) - k:
        return quickselect_rec(l, k, pivot_index + 1, right)

l = [5, 7, 4, 8, 3, 2, 1, 0, 9, 21, 41, 26, 5, 9, 4, 20]
quickselect(l, 1)
print(l)
