even_nums = filter(lambda x: x%2 == 0, range(1, 11))
print(list(even_nums))

# як можна замінити filter() на list comprehensions:

nums = [1, 2, 3, 4, 5, 6]
even_nums = [x for x in nums if x % 2 == 0]
print(even_nums)


def is_positive(x):
    return x>0

nums = [-2, -1, 0, 1, 2]
positive_nums = filter(is_positive, nums)
print(list(positive_nums))


some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'
new_str = "".join(list(filter(lambda x: x.islower(), some_str)))
print(new_str)

# list comprehensions Для рядка літер:

some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'
new_str = "". join([x for x in some_str if x.islower()])
print(new_str)