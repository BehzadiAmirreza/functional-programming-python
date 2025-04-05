def fib():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y
    
gen = fib()
for _ in range(100):
    print(next(gen))
