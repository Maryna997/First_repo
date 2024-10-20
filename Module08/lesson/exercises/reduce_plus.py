# We're going to calculate the years of experience that
# we made up with all the employees

import json
from functools import reduce
import pathlib

current_dir = pathlib.Path(__file__).parent

with open(current_dir/"employees.json") as json_file:
    data = json.load(json_file)

    total_years = reduce(lambda x, y: x + y["years_of_experience"], data, 0)

    print(total_years)