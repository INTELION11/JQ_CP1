# JQ 1st Flexible calculator  
  
# set up a counter (int) and a loop control flag (bool)  
div_counter = 0    
user_num = True    
choicing = True
  
# add all numbers using a loop and float conversion  
def plus(*nums):    
    total = 0    
    for num in nums:    
        total += float(num)    
    return total    
  
# find average by dividing the sum by the count  
def avg(*nums):    
    if len(nums) == 0:    
        return 0    
    return plus(*nums) / len(nums)    
  
# get the largest number using max() and float conversion  
def get_max(*nums):    
    return max(float(num) for num in nums)    
  
# get the smallest number using min() and float conversion  
def get_min(*nums):    
    return min(float(num) for num in nums)    
  
# multiply all numbers using a loop  
def mult(*nums):    
    result = 1    
    for num in nums:    
        result *= float(num)    
    return result    
  
# collect numbers from user input and store as list  
num_list = []    
while user_num:    
    div_counter += 1    
    number = input("What numbers would you like to include in this problem? When you're done, please say done\n").strip().lower()    
    if number == "done":    
        user_num = False    
    else:    
        try:    
            float(number)  # make sure input is a number  
            num_list.append(number)    
        except ValueError:    
            print("Error: Invalid input. Please enter numbers only.")    
  

# print numbers as a good string  
print(f"Numbers entered: {', '.join(num_list)}")    
  

# ask user for calculation type and perform the selected function  
action = input("Would you like to calculate the\n sum\n average\n max\n min\n product\n").strip().lower()    
  # if action is sum,avarage,max,min,product do its funtion, if not display try again
while choicing:
    action = input("Would you like to calculate the\n sum\n average\n max\n min\n product\n").strip().lower()   
    if action == "sum":    
        print(f"Sum: {plus(*num_list)}")  
        break  
    elif action == "average":    
        print(f"Average: {avg(*num_list)}")  
        break  
    elif action == "max":    
        print(f"Max: {get_max(*num_list)}")    
        break
    elif action == "min":    
        print(f"Min: {get_min(*num_list)}")    
        break
    elif action == "product":    
        print(f"Product: {mult(*num_list)}")    
        break
    else:    
        print("do it again.")
        continue   