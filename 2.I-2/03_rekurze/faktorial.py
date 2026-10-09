def faktorial(n):
    if n == 0 or n == 1:
        return 1
    lower = faktorial(n - 1)
    return lower * n

n = int(input())
print(faktorial(n))
