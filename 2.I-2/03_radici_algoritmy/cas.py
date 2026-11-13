import file_write_read  #  načetli jsme si do tohoto programu funkce z jiného programu
import bubble_sort
import select_sort
import insert_sort
import quciksort
import time



l1 = file_write_read.read_nums()
l2 = l1.copy()
l3 = l1.copy()


zacatek = time.time()
select_sort.select_sort(l1)
konec = time.time()
print("čas selectsort:", konec - zacatek, "s")

zacatek = time.time()
bubble_sort.bubble_sort2(l2)
konec = time.time()
print("čas bubblesort:", konec - zacatek, "s")

zacatek = time.time()
quciksort.quicksort(l3)
konec = time.time()
print("čas quicksort:", konec - zacatek, "s")
