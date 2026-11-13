def swap(l, a, b):
    temp = l[a]
    l[a] = l[b]
    l[b] = temp

def quicksort(nums):
    quicksort_rec(nums, 0, len(nums) - 1)
"""
TOTO ŘEŠENÍ NENÍ OPTIMÁLNÍ - zbytečně vytváříme nové seznamy

def quicksort_rec(nums, left, right):  
    if left >= right:
        return nums
    pivot_index = left
    left_list = []  # seznam čísel menších než pivot
    right_list = []  # seznam čísel větších než pivot
    for i in range(left + 1, right + 1):
        if nums[pivot_index] >= nums[i]:  # menší čísla dáváme do levé skupiny
            left_list.append(nums[i])
        elif nums[pivot_index] < nums[i]:  # větší čísla dáváme do pravé skupiny
            right_list.append(nums[i])
    nums = left_list + [nums[pivot_index]] + right_list  # sestavíme nový seznam - levá skupina, pivot, pravá skupina
    nums = quicksort_rec(nums, left, left + len(left_list) - 1)
    nums = quicksort_rec(nums, left + len(left_list) + 1, right)
    return nums
"""

def quicksort_rec(nums, left, right):
    if left >= right:
        return
    pivot_index = left
    left_pointer = left + 1
    right_pointer = right
    while left_pointer < right_pointer:
        while left_pointer < right_pointer and nums[left_pointer] <= nums[pivot_index]:
            left_pointer += 1
        while left_pointer < right_pointer and nums[right_pointer] > nums[pivot_index]:
            right_pointer -= 1
        if left_pointer < right_pointer:
            swap(nums, left_pointer, right_pointer)
    if nums[left_pointer] <= nums[pivot_index]:
        swap(nums, left_pointer, pivot_index)
        pivot_index = left_pointer
    elif nums[left_pointer] > nums[pivot_index]:
        swap(nums, left_pointer - 1, pivot_index)
        pivot_index = left_pointer - 1
    quicksort_rec(nums, left, pivot_index - 1)  # volání na levou část
    quicksort_rec(nums, pivot_index + 1, right)  # volání na pravou část
