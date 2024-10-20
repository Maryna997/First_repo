def log_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
            # raise  # re-throw the last exception

    return wrapper

@log_errors
def divide(x, y):
    return x / y

@log_errors
def f2():
    return "232d" - 1

@log_errors
def f3():
    raise SystemError("Enough for today")

divide(1, 0)
f2()
f3()


