from app_classes.user import User

def calculate_salaries(user_list: list[User]) -> int:
    salary_sum = 0
    for user in user_list:
        salary_sum += user.salary
    return salary_sum