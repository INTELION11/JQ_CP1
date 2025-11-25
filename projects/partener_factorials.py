# JQ 1st Factorials  
# spheudo code writter - isabella  
  
def function_factorial():  
    # asking user what number they want   
    user_num = input("What number do you want? ")  
  
    # checking if it's a number  
    try:  
        user_num = int(user_num)  # must be integer for factorial  
    except ValueError:  
        print("Please try again")  
        return  # stop function if not a number  
  
    # If number is an integer  
    print("wow you got a real number")  
  
    # list to collect numbers  
    num_list = []  
  
    # Getting all the numbers under using -1  
    for i in range(user_num, 0, -1):  
        num_list.append(i)  
  
    # multiplying them all together for the factorial  
    factored_number = 1  
    for num in num_list:  
        factored_number *= num  
  
    # Print first number  
    print(f"First number: {user_num}")  
    # print factored number  
    print(f"Factorial: {factored_number}")  
  
# Run the function  
function_factorial()  