from typing import Generator

def generate_numbers(n: int) -> Generator[int, None, str]:
    for i in range(n):
        yield i 
    return "End..."

# numbers_generator = generate_numbers(4)
# print(next(numbers_generator))
# print(next(numbers_generator))
# print(next(numbers_generator))
# print(next(numbers_generator))


'''
Написати функцію-генератор, яка буде отримувати імʼя через yield і повертати "Hello, {name}"
'''

def generate_welcomes() -> Generator[None, str, None]:
    while True:
        name = yield "Please enter name:"
        print(f"Welcome, {name}")

welcome_generator = generate_welcomes()

# while True:
#     name = input(next(welcome_generator))
#     welcome_generator.send(name)


# def generate_numbers_copy(n: int) -> Generator[int]:
#     for i in range(n):
#         yield i
#     return "End..."








