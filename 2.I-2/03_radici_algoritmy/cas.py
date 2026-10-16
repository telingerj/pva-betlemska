import file_write_read  #  načetli jsme si do tohoto programu funkce z jiného programu
import bubble_sort
import select_sort
import insert_sort
import time


l = file_write_read.read_nums()
zacatek = time.time()
#select_sort.select_sort(l)
l.sort()
konec = time.time()
print("čas:", konec - zacatek)

file_write_read.write_nums(l)
