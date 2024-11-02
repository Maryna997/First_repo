from dataclasses import dataclass
import json
'''
Створити клас, який буде зберігати інформацію про героя

(name. health)

Додати класи для зброї Weapon(damage)

Написати код, який буде серіалізувати героя у json
'''

@dataclass
class Weapon:
    damage: int

@dataclass
class Hero:
    name: str
    health: int
    weapon: Weapon

    # def to_json(self):
    #     return {"name": self.name, "health": self.health, "weapon": weapon.to_json()}



weapon = Weapon(100)
hero = Hero("Hero name", 200, weapon)

# print(dir(weapon))
# print(hero.__dict__)
# print(weapon.__dict__)

with open('hero.json', 'w') as json_file:
    json.dump(hero, json_file, default=lambda o: o.__dict__)