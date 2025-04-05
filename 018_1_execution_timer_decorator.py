import time

def log_execution(func):
    def wrapper(*args, **kwargs):
        # Format args for cleaner display
        args_str = ', '.join(map(str, args))
        print(f"Calling: {func.__name__}({args_str})")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.5f} seconds")
        return result
    return wrapper

@log_execution
def slow_function(n):
    time.sleep(n)
    return "Finished!"

@log_execution
def add(a, b):
    return a + b

# Call the functions
print(add(3, 4))
print(slow_function(4))
