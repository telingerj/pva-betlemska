def divide(l, left, right):
    less = []
    greater = []
    for i in range(1, len(l)):
        if l[i] < l[0]:
            less.append(l[i])
        elif l[i] >= l[0]:
            greater.append(l[i])
    print(less)
    print(greater)
    # TODO: použít rozsah left, right

l = [5, 4, 7, 8, 9, 6, 3, 2, 1, 0]
divide(l, 5, 9)
