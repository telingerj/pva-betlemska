def quicksort(nums):
    quicksort_rec(nums, 0, len(nums) - 1)

def quicksort_rec(nums, left, right):  # TOTO ŘEŠENÍ NENÍ OPTIMÁLNÍ - zbytečně vytváříme nové seznamy
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

nums = [5, 4, 7, 8, 9, 3, 2, 1]
quicksort(nums)
