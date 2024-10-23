class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def say_name(self) -> None:
        print(f'Hi! I am {self.name} and I am {self.age} years old.')

    def set_age(self, age: int) -> None:
        self.age = age

bob = Person('Boris', 34)

bob.say_name()
bob.set_age(25)
bob.say_name()



class Person:
    count = 0

    def __init__(self, name: str):
        self.name = name
        Person.count += 1

    def how_many_persons(self):
        print(f"Кількість людей зараз {Person.count}")

first = Person('Boris')
first.how_many_persons()
second = Person('Alex')
second.how_many_persons()


class Person:
    count = 0

    def __init__(self):
        self.count = 10
        
person = Person()
print(person.count)
print(Person.count)

# We can also write like this:

# class Person:      
#     count = 0

# person = Person()
# person.count = 10 
# print(person.count)  # 10
# print(Person.count)  # 0



class Pokemon:
    def __init__(self, name, type, health):
        self.name = name   # Ініціалізація атрибута імені
        self.type = type   # Ініціалізація атрибута типу
        self.health = health  # Ініціалізація атрибута здоров'я
    
    def attack(self, other_pokemon):
        print(f'{self.name} attacks {other_pokemon.name}!')

    def dodge(self):
        print(f'{self.name} dodged the attack!')

    def evolve(self, new_form):
        print(f'{self.name} is evolving into {new_form}!')
        self.name = new_form

# Створення об'єкта Pikachu
pikachu = Pokemon("Pikachu", "Electric", 100)

# Використання методів
pikachu.attack(Pokemon("Charmander", "Fire", 100))
pikachu.dodge()
pikachu.evolve("Raichu")