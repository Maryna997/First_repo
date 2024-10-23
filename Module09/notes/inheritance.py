class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age
        
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow"

class Dog(Animal):
    def __init__(self, nickname: str, age: int, breed: str):
        super().__init__(nickname, age)  # Викликаємо конструктор базового класу
                                         # we can call only nickname or age if needed
        self.breed = breed   # Додаємо нову властивість

    def make_sound(self) -> str:
        return "Woof"
    
    def chase_tail(self) -> str:
        return f'{self.nickname} is chasing its tail!'
    
class Cow(Animal):
    def make_sound(self) -> str:
        return "Moo"
    
my_cat = Cat("Simon", 4)
my_cow = Cow("Bessie", 3)

print(my_cat.make_sound()) 
print(my_cow.make_sound())  

my_dog = Dog("Rex", 5, "Golden Retriever")
print(my_dog.make_sound())  
print(my_dog.chase_tail())  


