class CountDown: 
    def __init__(self, start):
        self.current = start 

    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.current == 0:
            raise StopIteration
        self.current -= 1
        return self.current
    
if __name__ == "__main__":
    counter = CountDown(5)
    for count in counter:
        print(count)


# generator:
def count_down(start):
    current = start 
    current -= 1
    while current >= 0:
        yield current
        current -= 1

# Використання генератора
for count in count_down(5):
    print(count)




from random import randint

class RandIterator:
    def __init__(self, start, end, quantity):
        self.start = start
        self.end = end
        self.quantity = quantity
        self.count = 0 
    
    def __iter__ (self):
        return self
    
    def __next__(self):
        self.count += 1
        if self.count > self.quantity:
            raise StopIteration
        else: 
            return randint(self.start, self.end)
        
if __name__ == "__main__":
    my_random_list = RandIterator(1, 20, 5)

    for rn in my_random_list:
        print(rn, end = " ")



# generator
from random import randint

def rand_generator(start, end, quantity):
    count = 0
    while count < quantity:
        yield randint(start, end)
        count += 1

if __name__ == "__main__":
    for rn in rand_generator(1, 20, 5):
        print(rn, end=' ')
        
