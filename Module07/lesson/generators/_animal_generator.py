

def animal_generator():
    yield "Elephant"
    yield "Bird"
    yield "Lion"

gen = animal_generator()
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))