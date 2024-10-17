from collections import defaultdict
 
phone_numbers = [
    "0509993636",
    "0679993636",         
    "0959993636",
    "0969993636",
    "0509993637",
    "0639993636",
    "0509993632",
    "0339993632",
]

# phone_book = {}

# for number in phone_numbers:
#     if number.startswith(("050", "095")):
#         key = "Vodafone"
#         if key in phone_book:
#            phone_book[key].append(number)
#         else:
#            phone_book[key] = [number]
 
 
#     if number.startswith(("067", "096")):
#         key = "Kyivstar"
#         if key in phone_book:
#            phone_book[key].append(number)
#         else:
#            phone_book[key] = [number]


#     if number.startswith(("063", "093")):
#         key = "Life"
#         if key in phone_book:
#            phone_book[key].append(number)
#         else:
#            phone_book[key] = [number]

# print(phone_book)


phone_book = defaultdict(list)
for number in phone_numbers:
    if number.startswith(("050", "095")):
        phone_book["Vodafone"].append(number)
       
 
 
    if number.startswith(("067", "096")):
        phone_book["Kyivstar"].append(number)


    if number.startswith(("063", "093")):
       phone_book["Life"].append(number)

print(dict(phone_book))
print("Vodafone" in phone_book)
 
 