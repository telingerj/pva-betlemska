def numbers(n):
    if n == 0:
        print(0)
    else:
        numbers(n - 1)
        print(n)


numbers(10)
