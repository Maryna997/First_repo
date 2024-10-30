my_list = [1, 2, 3]

def square_list(x: list):
    return[el**2 for el in x]

new_list = square_list(my_list)
print(new_list)
print(my_list)



my_list = [1, 2, 3]
copy_list = my_list[:]
copy_list.append(4)
print(my_list, copy_list)

my_dict = {1: "a"}
copy_dict = {**my_dict}
copy_dict["new_key"] = "new_value"
print(my_dict, copy_dict)

