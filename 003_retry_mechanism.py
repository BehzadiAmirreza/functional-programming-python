import random

def retry(func, max_retries=3):
    """
    Returns a wrapped function that retries the original function on ValueError.
    """
    def wrapper():
        for attempt in range(1, max_retries + 1):
            try:
                result = func()
                print(f"Attempt {attempt}: Succeeded")
                return result
            except ValueError:
                print(f"Attempt {attempt}: Failed")
                if attempt == max_retries:
                    print("No more retries!")
                    return None
    return wrapper

def unstable_function():
    """Simulates an unstable function that fails 50% of the time."""
    if random.randint(0, 1) == 0:
        raise ValueError("Transient error!")
    return "Success!"

# Define the retry-wrapped function (do not call it here)
retry_unstable = retry(unstable_function, max_retries=3)

# Test the function
if __name__ == "__main__":
    print("Starting test...")
    result = retry_unstable()  # Call the function here
    print("Final result:", "Success" if result else "Failed")
