def fibonacci_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

def tribonacci_rec(n):
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    return tribonacci_rec(n - 1) + tribonacci_rec(n - 2) + tribonacci_rec(n - 3)


def fibonacci(n):
    l = [0, 1]
    for i in range(2, n + 1):
        l.append(l[i - 1] + l[i - 2])
    return l[n]

#TODO: implementovat tribonacciho posloupnost


cislo = int(input())
print(tribonacci_rec(cislo))

