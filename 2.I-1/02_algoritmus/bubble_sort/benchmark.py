from bubble_sort import *
from num_generator import read_nums
import time

l1 = read_nums("nums")
l2 = l1.copy()

start_time = time.time()
bubble_sort1(l1)
print("bubble sort 1:", time.time() - start_time)

start_time = time.time()
bubble_sort2(l2)
print("bubble sort 2:", time.time() - start_time)
