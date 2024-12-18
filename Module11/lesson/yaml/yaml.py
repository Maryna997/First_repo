import yaml

users = [
    {"name": "Микола", "age": 22, "gender": "male"},
    {"name": "Марія", "age": 22, "gender": "female"},
    {"name": "Назар", "age": 22, "gender": "male"},
]

with open("test.yaml", "w", encoding="utf-8") as f:
    yaml.dump(users, f, allow_unicode=True)

with open("test.yaml", "r", encoding="utf-8") as f:
    copy_users = yaml.load(f, Loader=yaml.FullLoader)

print(copy_users)