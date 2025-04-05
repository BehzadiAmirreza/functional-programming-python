def subtract(x, y):
    return x - y

def reverse_args(func):
    def reversed(x, y):
        return func(y, x)
    return reversed
    
reverse_subtract = reverse_args(subtract)
print(reverse_subtract(10, 5))  # Outputs: -5 (because it computes 5 - 10)
