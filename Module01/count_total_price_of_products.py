price_per_croissant = 1.04
price_per_glass = 0.34
price_per_coffee_pack = 4.42

num_croissants = int(input("Введіть кількість круасанів: "))
num_glasses = int(input("Введіть кількість склянок: "))
num_coffee_packs = int(input("Введіть кількість упаковок кави: "))

total_cost = num_croissants * price_per_croissant + \
             num_glasses * price_per_glass + \
             num_coffee_packs * price_per_coffee_pack  

total_dollars = int(total_cost)

print(f"Загальна вартість у повних доларах: {total_dollars} доларів")


