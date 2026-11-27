def merge(l, left, right, left_size, right_size):
    merged = [0] * (left_size + right_size)
    right_start = right - right_size + 1
    left_pointer = left
    right_pointer = right_start
    merged_pointer = 0
    while merged_pointer < len(merged):
        if right_pointer > right or l[left_pointer] <= l[right_pointer]:
            merged[merged_pointer] = l[left_pointer]
            left_pointer += 1
            merged_pointer += 1
        elif left_pointer == right_start or l[left_pointer] > l[right_pointer]:
            merged[merged_pointer] = l[right_pointer]
            right_pointer += 1
            merged_pointer += 1

    for i in range(len(merged)):
        l[i + left] = merged[i]
    print(merged)

l = [547, 899, 1, 3, 4, 2, 6, 8, 645, 48]
merge(l, 2, 7, 3, 3)
print(l)
