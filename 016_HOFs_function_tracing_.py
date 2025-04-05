def add(x, y):
    return x + y

def trace(func):
    def wrapper(*args, **kwargs):
        print(f"Calling `{func.__name__}` with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function `{func.__name__}` returned {result}")
        return result
    return wrapper

# Demonstrate the original add function
print("add(3, 4)")
print(add(3, 4))  # Output: 7

# Apply the trace wrapper to add
trace_add = trace(add)

# Demonstrate the traced add function
print("\ntrace_add = trace(add)")
print("trace_add(3, 4)")
print(trace_add(3, 4))