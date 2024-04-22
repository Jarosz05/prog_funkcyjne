import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {(end_time - start_time)} seconds")
        return result
    return wrapper

@timeit
def example_function():
    time.sleep(1)

example_function()
