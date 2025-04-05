from time import perf_counter

def timed(func):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()

        print(f"Function `{func.__name__}` took {round(end_time-start_time, 4)} seconds to execute.")
        return result

    return wrapper

@timed
def loop_this_many_times(n):
    for i in range(n):
        pass
    return "testing"

loop_this_many_times(10**6)
# Function loop_this_many_times took 0.0267 seconds to execute.

loop_this_many_times(10**7)
# Function loop_this_many_times took 0.2255 seconds to execute.

loop_this_many_times(10**8)
# Function loop_this_many_times took 2.2443 seconds to execute.
