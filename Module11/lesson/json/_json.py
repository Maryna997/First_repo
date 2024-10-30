# serialization: 
# load -> in File
# loads -> in string

# deserialization:
# dump -> in File
# dumps -> in string 

  
import json 

d = {"a": 1}
l = [1, 2.2]
t = (3, 4)
s = "I am string!"
b = True
st = {1, 2, "Test"}
obj = {"tuple": t, "list": l, "dict": d, "string": s, "bool": b}
print(json.dumps(d))
print(json.dumps(l))
print(json.dumps(t))
print(json.dumps(s)) 
print(json.dumps(b))

with open("storage.json", "w") as f:
    json.dump(obj, f)



data = {"developer": {"name": "Юрій Кучма", "species": "програміст"}}

with open("data_user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)

with open("data_user.json", "r", encoding="utf-8") as f:
    restore_data = json.load(f)
    print(restore_data)



person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programmer"],
}

# convert into JSON:
person_json = json.dumps(person)
# use different formatting style
person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True)

# the result is a JSON string:
print(person_json)
print(person_json2)



json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data = json.loads(json_string)
print(type(data))
print(data["researcher"] ["name"])


import pickle 

class User:
    # Custom class with all class variables given in the __init__()
    def __init__(self, name, age, active):
        self.name = name
        self.age = age
        self.active = active

    # def toJSON(self):
    #     return {
    #         "name": self.name,
    #         "age": self.age,
    #         "active": self.active
    #     }

    def to_json(self):
        return self.__dict__
    
    # def __getstate__(self):
    #     pass

    # def __setstate__(self):
    #     pass

leo = User("Leo", 24, True)

print(leo.__dict__)

# serialized_leo = json.dumps(leo.__dict__)
# serialized_leo = json.dumps(leo.toJSON())
#print(serialized_leo)


with open("info.bin", "wb") as f:   # wb = write byte (always with files with bytes)
    pickle.dump(leo, f)

with open("info.bin", "rb") as f:
    res = pickle.load(f) 
    print(res)
    print(res.to_json())


        