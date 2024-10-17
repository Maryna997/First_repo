def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))


def count_down(start):
    while start > 0:
        yield start 
        start -= 1
for number in count_down(5):
    print(number)
