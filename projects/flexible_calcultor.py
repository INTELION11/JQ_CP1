# JQ 1st Flexible calculator  
div_counter = 0  
user_num = True  
  
# Sum  
def plus(*nums):  
    total = 0  
    for num in nums:  
        total += float(num)  
    return total  
  
# Average  
def avg(*nums):  
    if len(nums) == 0:  
        return 0  
    return plus(*nums) / len(nums)  
  
# Max  
def get_max(*nums):  
    return max(float(num) for num in nums)  
  
# Min  
def get_min(*nums):  
    return min(float(num) for num in nums)  
  
# Product  
def mult(*nums):  
    result = 1  
    for num in nums:  
        result *= float(num)  
    return result  
  
num_list = []  
while user_num:  
    div_counter += 1  
    number = input("What numbers would you like to include in this problem? When you're done, please say done\n").strip().lower()  
    if number == "done":  
        user_num = False  
    else:  
        try:  
            float(number)  
            num_list.append(number)  
        except ValueError:  
            print("Error: Invalid input. Please enter numbers only.")  
  
print(f"Numbers entered: {', '.join(num_list)}")  
  
action = input("Would you like to calculate the\n sum\n average\n max\n min\n product\n").strip().lower()  
  
if action == "sum":  
    print(f"Sum: {plus(*num_list)}")  
elif action == "average":  
    print(f"Average: {avg(*num_list)}")  
elif action == "max":  
    print(f"Max: {get_max(*num_list)}")  
elif action == "min":  
    print(f"Min: {get_min(*num_list)}")  
elif action == "product":  
    print(f"Product: {mult(*num_list)}")  
else:  
    print("Invalid action.") 