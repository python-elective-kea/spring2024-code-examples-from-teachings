from functools import wraps
from datetime import datetime

def log_function_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = func(*args, **kwargs)
        with open("function_log.txt", "a") as f:
            f.write(f"Timestamp: {timestamp}, Args: {args}, Result: {result}\n")
        return result
    return wrapper

@log_function_data
def add(*args):
    return sum(args)

print(add(1, 2, 3))  # This will log the timestamp, args (1, 2, 3), and result (6) to the file.

@log_function_data
def printer(text):
    return text

print(printer("Hello, World!"))  # This should log the timestamp, the argument ("Hello, World!"), and the result ("Hello, World!") to the file.
