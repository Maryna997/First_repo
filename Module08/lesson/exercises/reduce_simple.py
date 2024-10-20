# We're going to calculate the years of experience that
# we made up with all the employees

import json
import pathlib

current_dir = pathlib.Path(__file__).parent

with open(current_dir/"employees.json") as json_file:
    data = json.load(json_file)

    total_years = 0

    for i in range(len(data)):
        total_years += data[i]["years_of_experience"]

    print(total_years)