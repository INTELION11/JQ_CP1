# JQ 1st Order up
# meal,drink,side checkers is true
meal_check = True   
drink_check = True
Side_check = True
# def check(items ordered) 
# total is sum of items
#for items in dictionary order
# print items and price
# print total
def check(ordered):
    total = sum(ordered.values())
    for items in ordered:
          print(f"{items} :::: {ordered[items]}")
         # total += order[items]
    print(f"your total is {total}")
    # dictionary order is {}
order = {
 
}
# meal is burgers: price,
meal = {
    "cheeseburger": 5.00,
    "bacon burger": 6.00,
    "double-double":3.00,
    "shackburger": 12.00,
    "butterburger": 4.00
}
#drinks is drink:price,
drink = {
    "lemonade": 2.50,
    "milkshake": 2.50,
    "soda": 3.00,
    "tap water": 2.00,
    "orange juice": 4.00
}
# side dishes is side:price,
side_dishes = {
    "american fries": 1.00,
    "mashed potatoes": 3.00,
    "bread": 3.00,
    "onion rings": 2.50,
    "mac and cheese": 12.00
}
# display welcome to the restaurnat you can press quit at any time
print(" Welcome to [insert name] Restaurant, pleaese type quit at any time to quit, what would you like to")
# meal check while loop
while meal_check == True:
    # display menu
    for key in meal.keys():
        print(f"{key} is {meal[key]}")
    print("")
    # ask user what item to buy
     # if answer is quit, quit
    # check if item is in menue
    #add meal and price to order dictionary
    # meal check is false
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
 # display menu
while drink_check == True:
    for key in drink.keys():
            print(f"{key} is {drink[key]}")
    print("")
        # ask user what item to buy
     # if answer is quit, quit
    # check if item is in menue
    #add meal and price to order dictionary
    # meal check is false
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
    
  # display menu   
while Side_check == True:
    for key in side_dishes.keys():
            print(f"{key} is {side_dishes[key]}")
    print("")
    # ask user what item to buy
     # if answer is quit, quit
    # check if item is in menue
    #add meal and price to order dictionary
    # meal check is false
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
         # display menu
Side_check = True
while Side_check == True:
    for key in side_dishes.keys():
            print(f"{key} is {side_dishes[key]}")
    print("")
    # ask user what item to buy
     # if answer is quit, quit
    # check if item is in menue
    #add meal and price to order dictionary
    # meal check is false
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
        Side_check = False
# call check function
check(order)
