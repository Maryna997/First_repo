import csv 

with open("users.csv", "w") as f:
    columns = ["name", "surname", "gender"]
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()
    writer.writerow({"name": "Rory", "surname": "Gilmore", "gender": "w"})

with open("users.csv") as f: 
    reader = csv.DictReader(f)
    print(reader)
    users = list(reader)
    print(users)

    # for user in reader:    if we want to see one row 
    #     print(user)


