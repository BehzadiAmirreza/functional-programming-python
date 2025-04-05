def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci is only defined for non-negative integers.")
    if n in (0, 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(9))