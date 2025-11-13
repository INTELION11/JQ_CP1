# JQ 1st Order up
meal_check = True   
drink_check = True
Side_check = True
def check(ordered):
     
     for items in ordered:
          print(f"{items} :::: {ordered[items]}")
          total += ordered[items]
          print(f"your total is {total}")
     
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

while meal_check == True:
    for key in meal.keys():
        print(f"{key} is {meal[key]}")
    print("")
    action = input("what meal would you like\n ").strip().lower()
    if action == "quit":
        quit()
    if action not in meal:
        print("please try again")
        continue
    else:
        order[f"{action}"] = meal[action]
        print(order)
        meal_check = False
    print("")

while drink_check == True:
    for key in drink.keys():
            print(f"{key} is {drink[key]}")
    print("")
    
    action = input("what drink would you like\n ").strip().lower()
    if action == "quit":
        quit()
    if action not in drink:
        print("please try again")
        continue
    else:
        order[f"{action}"] = drink[action]
        print(order)
        drink_check = False
    
    
while Side_check == True:
    for key in side_dishes.keys():
            print(f"{key} is {side_dishes[key]}")
    print("")

    action = input("what side dish would you like\n ").strip().lower()
    if action == "quit":
        quit()
    if action not in  side_dishes:
        print("please try again")
        continue
    else:
        order[f"{action}"] = side_dishes[action]
        print(order)
        Side_check = False
Side_check = True
while Side_check == True:
    for key in side_dishes.keys():
            print(f"{key} is {side_dishes[key]}")
    print("")

    action = input("what side dish would you like\n ").strip().lower()
    if action == "quit":
        quit()
    if action not in  side_dishes:
        print("please try again")
        continue
    if action in order:
         print("You have already ordered this item, please try again\n ")
         continue
    else:
        order[f"{action}"] = side_dishes[action]
        print(order)
        Side_check = False

check(order)
