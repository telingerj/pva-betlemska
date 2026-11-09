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

l = [5, 4, 7, 8, 9, 6, 3, 2, 1, 0]
divide(l, 0, len(l) - 1)
