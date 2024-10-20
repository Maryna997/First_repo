from functools import wraps

'''
Написати декоратор, який буде виводити аргументи функції

my_function(1, 2, 3, 4, 5)

Calling function 'my_function'
With arguments 1, 2, 3, 4, 5
'''

def print_arguments(function):
    @wraps(function)   # wraps allows us not to loose info about our function. It's decorator for decorator
    def wrapper(*args, **kwargs):
        # print(args, kwargs)
        print(f'Calling {function.__name__}')
        result = function(*args, **kwargs)
        print(result)
        return result
    return wrapper

@print_arguments
def my_function(one, two, three, four=4, five="five"):
    return "Hello"
print(my_function.__name__)     # without wraps it would be the name of the decorator print_arguments

result = my_function(1, 2, 3, 4, 5)
print(result + " world!")


arguments = ["one", 2, "Three", [1, 2, 3]]
# print(*arguments)

list_1 = [1, 2, 3]
list_2 = [*list_1, 6, 7]
# print(list_2)


# print(my_function.__name__)
# print(my_function.__doc__)
my_other_function.__name__ = "hello"    # how to change name of the function. Be careful with that not to break the whole code
print(my_other_function.__name__)

