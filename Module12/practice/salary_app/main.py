from app_classes.user import User
from helper_functions.salary_helpers import calculate_salaries
# from colorama import Fore, Style

john = User("John", 1000)
jack = User("Jack", 2000)

print(calculate_salaries([john, jack]))

while True:
    user_input = input("enter command: ").strip()
    if user_input == 'salaries':
        print(calculate_salaries([john, jack]))
    elif user_input == 'exit':
        print('Goodbye!')
        break


# def main_loop():
#     while True:
#         user_input = input(Fore.BLUE + "enter command: " + Style.RESET_ALL ).strip()
#         if user_input == 'salaries':
#             print(calculate_salaries([john, jack]))
#         elif user_input == 'exit':
#             print('Goodbye!')
#             break