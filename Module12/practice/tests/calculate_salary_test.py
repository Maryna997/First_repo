from salary_app.app_classes.user import User
from salary_app.helper_functions.salary_helpers import calculate_salaries

john = User("John", 1000)
jack = User("Jack", 2000)

print(3000 == calculate_salaries([john, jack]))