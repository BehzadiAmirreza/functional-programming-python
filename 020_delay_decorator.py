import time
import functools
import uuid

# Dictionary to track delays for each user
user_delays = {}

def delay_decorator(func):
    @functools.wraps(func)
    def wrapper(user_id, resource):
        # Get the current delay for the user, default to 0
        delay = user_delays.get(user_id, 0)
        
        # Print the delay message if greater than 0
        if delay > 0:
            print(f"Your download will start in {delay}s...")
            time.sleep(delay)
        
        # Call the original function
        result = func(user_id, resource)
        
        # Update the delay for the user (double it)
        user_delays[user_id] = delay * 2 if delay > 0 else 1
        
        return result
    return wrapper

@delay_decorator
def download(user_id, resource):
    return f"Your resource is ready at: andybek.com/{uuid.uuid4()}"

# Example Usage
print(download("user123", "resource1"))
print(download("user123", "resource2"))
print(download("user123", "resource2"))
print(download("user456", "resource1"))
