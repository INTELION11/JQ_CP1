# JQ 1st Flexible calculator
div_counter = 0
user_num = True
# Sum
#Average
#Max
#Min
#Product

def plus(list):
    total = sum(list)
    return total

num_list = []
while user_num == True:
    div_counter += 1
    number = input(" what numbers would you like to include in this problem?, when your done please say done\n").strip().lower()
    if number == "done":
        user_num = False
    else:
        try:
            float(number)
            num_list.append(number)

        except ValueError:
            print("Error: Invalid input. Please enter integers only.")
        
    
print(num_list)

action = input(" would you like to calculate the\n sum\n avarage\n max\n min\n product\n").strip().lower()
#for num in num_list:
if action == "sum":
    print(plus(num_list))











