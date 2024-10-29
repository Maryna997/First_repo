import pickle

# Об'єкт для серіалізації
my_data = {"key": "value", "num": 42}

# Серіалізація об'єкта в байтовий рядок
serialized_data = pickle.dumps(my_data)
# Виведе байтовий рядок
print(serialized_data)

# Десеріалізація об'єкта з байтового рядка
deserialized_data = pickle.loads(serialized_data)
# Виведе вихідний об'єкт Python
print(deserialized_data)



# Об'єкт для серіалізації
my_data = {"key": "value", "num": 100}

# Серіалізація об'єкта в файл
with open("data.pickle", "wb") as file:
    pickle.dump(my_data, file)


# Десеріалізація об'єкта з файлу
with open("data.pickle", "rb") as file:
    deserialized_data = pickle.load(file)

# Виведе вихідний об'єкт Python
print(deserialized_data)


class Human:
    def __init__(self, name):
        self.name = name

bob = Human("Bob")
with open("instance.pickle", "wb") as file:
    pickle.dump(bob, file)


with open("instance.pickle", "rb") as file:
    loaded_instance = pickle.load(file)

print(loaded_instance.name)


# Збереження налаштувань
settings = {"theme": "dark", "language": "ukrainian"}
with open("settings.pickle", "wb") as f:
    pickle.dump(settings, f)

# Завантаження налаштувань
with open('settings.pickle', 'rb') as f:
    loaded_settings = pickle.load(f)

print(loaded_settings)