# JQ 1st Shopping List Manager

shopping_list = []

while True:
   
    action = input("add, remove, print, exit \n").strip().lower()
    if  action == "add":
     new_item = input("What item would you like to add?\n ")
     shopping_list.append(new_item)
    elif action == "remove":
       print(shopping_list)
       removing = input("what item would you like to remove? \n")
       if removing in shopping_list:
        shopping_list.remove(removing)
       else: 
          print("dont worry, your mom still loves you, please try again next time")
    elif action == "print":
       print(shopping_list)
    elif action == "exit":
        break
    else:
       print("you clearly failed english class, please try again")