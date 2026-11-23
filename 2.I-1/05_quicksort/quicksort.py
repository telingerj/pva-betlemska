"""
def divide(l, left, right):
    less = []
    greater = []
    for i in range(left + 1, right + 1):
        if l[i] < l[left]:
            less.append(l[i])
        elif l[i] >= l[left]:
            greater.append(l[i])
    l = less + [l[left]] + greater
    print(less)
    print(greater)
    print(l)
"""

def swap(l, i, j):  # prohodí hodnoty v seznamu l na indexech i a j
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

def quicksort(l):
    quicksort_rec(l, 0, len(l) - 1)

def quicksort_rec(l, left, right):
    if left >= right:
        return
    pivot_index = left
    left_pointer = left + 1  # levá šipka
    right_pointer = right  # pravá šipka
    while left_pointer < right_pointer:
        while left_pointer < right_pointer and l[left_pointer] <= l[pivot_index]:
            left_pointer += 1
        while left_pointer < right_pointer and l[right_pointer] > l[pivot_index]:
            right_pointer -= 1
        swap(l, left_pointer, right_pointer)
    #TODO: dejte pivota na správné místo - mezi obě skupiny
    swap(l, left_pointer - 1, pivot_index)  # tady opravit
    pivot_index = left_pointer - 1
    quicksort_rec(l, left, pivot_index - 1)
    quicksort_rec(l, pivot_index + 1, right)



l = [5, 4, 7, 8, 9, 6, 3, 2, 1, 0]
quicksort(l)
print(l)
