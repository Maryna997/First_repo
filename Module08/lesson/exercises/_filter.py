a = [i for i in range (100)]
print(a)
filter(lambda x: x % 2 == 0, a)
print(list(filter(lambda x: x % 2 == 0, a)))    # we write list not to hve just filter object 

