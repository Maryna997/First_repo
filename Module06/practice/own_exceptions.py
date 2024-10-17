
try:
    result = 1000/0
    print(result)
except ZeroDivisionError:
    print("Zero division exception")
# або except Exception:
#         print("Exception occurred!")


'''
Написати бота, який буде порівнювати вік людини
'''

class TooYoungError(ValueError):
    pass

class NameTooShortError(Exception):
    pass

class SurnameTooShortError(ValueError):
    pass

def main():
    while True:
        age = int(input("Enter your age:"))
        if age < 18:
            #print("You're too young")
            raise TooYoungError("You're too young")
        name = input("Enter your name:")
        if len(name) < 3:
            #print("Name is too short")
            raise ValueError("Name is too short")
        surname = input("Enter your surname:")
        if len(surname) < 5:
            raise SurnameTooShortError("Surname is too short")


try:
    main()
except TooYoungError:
    print("You're too young")
except NameTooShortError:
    print("Name is too short")
except ValueError as error:
    print(error)


