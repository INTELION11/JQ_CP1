#JQ 1st Factorials
#spheudo code writter - isabella
#def function_factorial():
def function_factorial():
#asking user what number they want 
    user_num = input(" What number do you want?")
# cheking if its a number -
# Jacob - I chose to use try and exept for cheking if its a number
    try:
        # i had to use int isntead of float so that it was an intiger
        int(user_num)
    except ValueError:
        print("Please try again")
#              ()float
# If number is a real number
    if user_num is int:
#     display (Wow you got a number!)
        print("wow you got a real number")
    else:
#else:
        print("PLEASE try again")
        continue
 #  display(try again) Send user back up
 #      list()
    num_list = []
#Getting all the numbers under using -1
    counter = 0
    counter += 1
    num_list.append(user_num - counter)
# Putting the numbers in a list
#multiplying them all together
# Print first number
#print factored number