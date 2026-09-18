def a(x):  # předáváme funkci číslo - číslo se zkopíruje a uloží do proměnné x
    print(x)
    x = 2
    print(x)

def b(x):  # předáváme funkci seznam - seznam se nezkopíruje, předá se pouze reference na něj
    print(x)
    x[0] = 2  # když seznam upravíme, změna se projeví i v místě, kde jsme funkci volali
    print(x)

def swap(l, a, b):
    temp = l[a]
    l[a] = l[b]
    l[b] = temp


def is_sorted(l):
    for i in range(0, len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True

cislo = 1
seznam = [1, 2, 3, 4, 5]
a(cislo)
print(cislo)
b(seznam)
print(seznam)


seznam2 = [4, 2, 3, 5, 1]
print(is_sorted(seznam2))
swap(seznam2, 0, 4)
swap(seznam2, 3, 4)
print(seznam2)
print(is_sorted(seznam2))