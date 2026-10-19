def faktorial(n):
    if n == 0 or n == 1:
        return 1
    return n * faktorial(n - 1)

print(faktorial(3))
