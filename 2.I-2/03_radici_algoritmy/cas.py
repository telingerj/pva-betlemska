import file_write_read  #  načetli jsme si do tohoto programu funkce z jiného programu
import bubble_sort
import time


l = file_write_read.read_nums()
zacatek = time.time()
bubble_sort.bubble_sort1(l)
konec = time.time()
print("čas:", konec - zacatek)
