import datetime
now = datetime.datetime.now()
print(now)

from datetime import datetime

current_datetime = datetime.now()
print(current_datetime.date())
print(current_datetime.time())

import datetime
date_part = datetime.date(2024, 10, 1)
time_part = datetime.time(14, 50, 47)
combined_datetime = datetime.datetime.combine(date_part, time_part)
print(combined_datetime)

import datetime
specific_date = datetime.datetime(year=2013, month=2, day=9)
print(specific_date)

import datetime
specific_date = datetime.datetime(year=2013, month=2, day=9, hour=14, minute=30, second=15)
print(specific_date)

from datetime import datetime
now = datetime.now()
day_of_week = now.weekday()
print(f"Сьогодні:{day_of_week}")

from datetime import datetime
datetime1 = datetime(2015, 10, 3, 14, 25, 0)
datetime2 = datetime(2015, 10, 2, 14, 25, 0)

print(datetime1 == datetime2)
print(datetime1 != datetime2)
print(datetime1 > datetime2)
print(datetime1 < datetime2)

from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta)

from datetime import datetime
seventh_day2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day2020 = datetime(year=2020, month=1, day=7, hour=14)

difference = seventh_day2020 - seventh_day2019
print(difference)
print(difference.total_seconds())

from datetime import datetime, timedelta
now = datetime.now()
future_date = now + timedelta(days=10)
print(future_date)

from datetime import datetime, timedelta
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
four_weeks_interval = timedelta(weeks=4)

print(seventh_day_2020 + four_weeks_interval)
print(seventh_day_2020 - four_weeks_interval)

from datetime import datetime
date = datetime(year=2024, month=10, day=1)

ordinal_number = date.toordinal()
print(f"Порядковий номер дати {date} становить {ordinal_number}")

from datetime import datetime
now = datetime.now()

ordinal_number = now.toordinal()
print(f"Порядковий номер дати {now} становить {ordinal_number}")

from datetime import datetime
napoleon_burns_moscow = datetime(year=1812, month=9, day=14)
current_date = datetime.now()
days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
print(days_since) 

from datetime import datetime
now = datetime.now()
timestamp = datetime.timestamp(now)
print(timestamp)

from datetime import datetime
timestamp = 1617183600
dt_object = datetime.fromtimestamp(timestamp)
print(dt_object)

from datetime import datetime
now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)
formatted_date_only = now.strftime("%A, %d %B %Y")
print(formatted_date_only)
formatted_time_only = now.strftime("%I:%M %p")
print(formatted_time_only)
formatted_date_only = now.strftime("%d.%m.%Y")
print(formatted_date_only)

from datetime import datetime
date_string = "2023.03.14"
datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
print(datetime_object)

from datetime import datetime
now = datetime.now()
iso_format = now.isoformat()
print(iso_format)

from datetime import datetime
iso_date_string = "2024-10-01T16:26:41.324637"
date_from_iso = datetime.fromisoformat(iso_date_string)
print(date_from_iso)

from datetime import datetime
now = datetime.now()
day_of_week = now.isoweekday()
print(f"Сьогодні: {day_of_week}")

from datetime import datetime
now = datetime.now()
iso_calendar = now.isocalendar()
print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar [2]} ")

from datetime import datetime, timezone
local_now = datetime.now()
utc_now = datetime.now(timezone.utc)
print(local_now)
print(utc_now)

from datetime import datetime, timezone, timedelta
utc_time = datetime.now(timezone.utc)
eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
print(eastern_time)

from datetime import datetime, timezone, timedelta
local_timezone = timezone(timedelta(hours=2))
local_time = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)
utc_time = local_time.astimezone(timezone.utc)
print(utc_time)

from datetime import datetime, timezone, timedelta
timezone_offset = timezone(timedelta(hours=2))
timezone_datetime = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)
iso_format_with_timezone = timezone_datetime.isoformat()
print(iso_format_with_timezone)

import time
current_time = time.time()
print(f"Поточний час: {current_time}")

import time
print("Початок паузи")
time.sleep(1)
print("Кінець паузи")

import time
current_time = time.time()
print(f"Поточний час: {current_time}")
readable_time = time.ctime(current_time)
print(f"Читабельний час: {readable_time}")

import time
current_time = time.time()
print(f"Поточний час: {current_time}")
local_time = time.localtime(current_time)
print(f"Місцевий час: {local_time}")

import time
start_time = time.perf_counter()

for _ in range (1_000_000):
    pass

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд")

a = 1_000_000
print(a)

import random
dice_roll = random.randint(1, 6)
print(f"Ви кинули {dice_roll}")

import random
num = random.random
print(num)

import random
fill_percentage = random.random() * 100
print(f"Заповнення: {fill_percentage:.2f}%")

import random
target = random.randrange(1, 11, 2)
print(f"Ціль: {target}")

import random 
cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]
random.shuffle(cards)
print(f"Перемішана колода: {cards}")

import random
fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits))
chosen_fruit = random.choices(fruits, k=1)
print(chosen_fruit)
chosen_fruits = random.choices(fruits, k=2)
print(chosen_fruits)

import random
colors = ["red", "green", "blue"]
weights = [11, 12, 10]
chosen_color = random.choices(colors, weights, k=1)
print(chosen_color)

import random
participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
team = random.sample(participants, 4)
print(f"Команда: {team}")

import random
price = random.uniform(50, 100)
print(f"Випадкова ціна: {price:.2f}")

import math
x = 3.7
ceil_result = math.ceil(x)
floor_result = math.floor(x)
trunc_result = math.trunc(x)
print(ceil_result, floor_result, trunc_result)

import math
print(math.pi)
angle = math.radians(60)
print(math.sin(angle))
print(math.sqrt(9))
print(math.log(10, 2))

import math
r = math.isclose(0.1 + 0.2, 0.3)
print(r)


# Praktyka:
def days_between_two_dates (date_one: str, date_two: str) -> int:
    result = datetime(2024, 6, 10).date() - datetime(2024, 5, 10).date()
    print(result)

# it's also possible to do like this:
# date_one_datetime = datetime.strptime(date_one, "%d-%m-%Y")
# date_two_datetime = datetime.strptime(date_two, "%d-%m-%Y")
# return (date_one_datetime - date_two_datetime).days 

print(days_between_two_dates("10.06.2024", "10.05.2024"))

# calculate age 
def calculate_persons_age(birthday_date: datetime) ->int:
    """A function to calculate persons age"""
    today = datetime.now().date()
    # days = (today - birthday_date.date()).days
    age = today.year - birthday_date.year 

# if (today.month < birthday_date.month) or (today.day < birthday_date.day)
# if (today.month < birthday_date.month) or (today.month == birthday_date.month and today.day < birthday_date.day)

    if ((today.month, today.day) < (birthday_date.month, birthday_date.day)):
        age -= 1

    if age < 0:
        age = 0

    return age 

person_one_birthday = datetime(2000, 1, 1)  #age = 24
person_two_birthday = datetime(2024, 9, 5)  #age = 0
person_three_birthday = datetime(2023, 10, 4)  #age = 1
person_four_birthday = datetime(2023, 11, 4)  #age = 0
person_five_birthday = datetime(2025, 10, 10)  #age = 0

print(calculate_persons_age(person_one_birthday))
print(calculate_persons_age(person_two_birthday))
print(calculate_persons_age(person_three_birthday))
print(calculate_persons_age(person_four_birthday))
print(calculate_persons_age(person_five_birthday))


# Написти функцію яка буде генерувати випадковий пароль потрібної довжини
# Пароль має містити як мінімум одну малу літеру, одну велику літеру та один спец-символ
import re 
import random 

def generate_random_password(password_length: int) -> str:
    if password_length <=2:
        raise ValueError
    
    password = ""
    for i in range (0, password_length -2):
        password += chr(random.randint(97, 122))   #97, 122 z ASCII
    
    uppercase_letter = chr(random.randint(65, 90))   # z ASCII for big letters
    special_character = chr(random.randint(33, 47))   # z ASCII for special characters 

    return password + uppercase_letter + special_character

print(generate_random_password(8))


# другий спосіб на розв*язання завдання 
import re 
import random 
import string 

# def generate_random_password_alternative():
    # password.append(random.choice(string.ascii_letters + string.digits + '@#$%^&+='))

def generatepassword():
    password = []
    for i in range(8):
        password += (random.choice(string.ascii_letters + string.digits + '@#$%^&+='))
    return ''.join(password)

print(generatepassword)
 
# в цьому варіанті часом можуть не додаватися спец-символи, але загалом цей варіант кращий