from typing import Callable

def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function

my_func = outer_function("Hello, world!")
my_func()



def counter() -> Callable[[], int]:
    count = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count
    
    return increment

count_calls = counter()

print(count_calls())
print(count_calls())
print(count_calls())