from collections import Counter
'''
В нас є список чисел, потрібно написати функцію, яка буде рахувати кількість повторень чисел
'''

numbers = [5, 0, 1, 2, 1, 1, 2, 2, 3, 5, 0]

# 1) Пройтися по усім числам у списку
# 2.1) Якщо число ще не зустрічалось, потрібно йому здати значення 1
# 2.2) Якщо число вже зустрічалось, потрібно взяти попереднє значення і збільгити його на 1
# 3) Зберегти інфу
# 4)Повернути значення

def count_numbers_in_a_list(numbers_list: list[int]) -> dict:
    counted_numbers = dict()
    for number in numbers_list:
        if number in counted_numbers: 
            counted_numbers[number] += 1
        else:
            counted_numbers[number] = 1
    return counted_numbers

print(count_numbers_in_a_list(numbers))

def count_numbers_in_a_list_alternative(numbers_list: list[int]) -> dict:
    return Counter(numbers_list)
#print(count_numbers_in_a_list_alternative(numbers))

result_dict = count_numbers_in_a_list_alternative(numbers)
print(result_dict[5])
