def binary_search(l, num):
    left = 0
    right = len(l) - 1
    return binary_search_rec(l, left, right, num)  # hledání v celém seznamu


def binary_search_rec(l, left, right, num):
    if left == right:
        if num == l[left]:
            return left
        return -1
    if left > right:
        return -1
    mid = (left + right) // 2
    if l[mid] > num:
        return binary_search_rec(l, left, mid - 1, num)
    elif l[mid] < num:
        return binary_search_rec(l, mid + 1, right, num)
    else:
        return mid


l = [5, 10, 15, 20, 21, 26, 30]
print(binary_search(l, 22))
