# JQ 1st Order up
order = {
      
}
meal = {
    "cheeseburger": 5.00,
    "bacon burger": 6.00,
    "double-double":3.00,
    "shackburger": 12.00,
    "butterburger": 4.00
}
drink = {
    "lemonade": 2.50,
    "milkshake": 2.50,
    "soda": 3.00,
    "tap water": 2.00,
    "orange juice": 4.00
}
side_dishes = {
    "american fries": 1.00,
    "mashed potatoes": 3.00,
    "bread": 3.00,
    "onion rings": 2.50,
    "mac and cheese": 12.00
}
print(" Welcome to [insert name] Restaurant, pleaese type quit at any time to quit, what would you like to")
for key in meal.keys():
        print(f"{key} is {meal[key]}")
print("")
action = input("what meal would you like ").strip().lower()
if action == "quit":
    quit()
elif action != side_dishes:
     print("please try again")
else:
    order[f"{action}"] = meal[action]
    print(order)
print("")
for key in drink.keys():
        print(f"{key} is {drink[key]}")
print("")
action = input("what drink would you like ").strip().lower()
if action == "quit":
    quit()
elif action != side_dishes:
     print("please try again")
else:
    order[f"{action}"] = drink[action]
    print(order)
for key in side_dishes.keys():
        print(f"{key} is {side_dishes[key]}")
print("")
action = input("what side dish would you like ").strip().lower()
if action == "quit":
    quit()
elif action != side_dishes:
     print("please try again")
else:
    order[f"{action}"] = side_dishes[action]
    print(order)

