def fibonacci(n):
    f = [0, 1]
    while len(f) <= n:
        f.append(f[-1] + f[-2])
    return f[-1]

def fibonacci_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)



print(fibonacci_rec(35))
print(fibonacci(35))
