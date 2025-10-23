#JQ 1st Paasword streinth  
#password is ask "what is your password"  
#points = 0  
while True:  
    password = input("what is your password \n").strip()  # ask for password and clean it  
    points = 0  # start points at zero  
  
    #length = len(password)  
    #list special_character  
    #list numbers  
    #characters is list(password)  
    #loop for letter in characters  
  
    special_characters = "!@#\$%^&*()_+-=[]{|;:,}.<>?)"  # all the weird symbols  
    numbers = "1234567890"  # just the digits for checking  
    # set up flags to see if each thing is found  
    has_num = False  # did we see a number yet  
    has_special = False  # did we see a special character yet  
    has_upper = False  # any uppercase found  
    has_lower = False  # any lowercase found  
  
    # go through each character in password  
    for char in password:  
        # if it's a number, remember that  
        if char in numbers:  
            has_num = True  
        # if it's a special, remember that  
        if char in special_characters:  
            has_special = True  
        # if uppercase, mark it  
        if char.isupper():  
            has_upper = True  
        # if lowercase, mark it  
        if char.islower():  
            has_lower = True  
  
    #if length >= 8 then points += 1  
    if len(password) >= 8:  # long enough  
        points += 1  
    #if has_num == True then points += 1  
    if has_num:  # saw a number  
        points += 1  
    #if has_special == True then points += 1  
    if has_special:  # saw a special char  
        points += 1  
    #if has_upper == True then points += 1  
    if has_upper:  # saw uppercase  
        points += 1  
    #if has_lower == True then points += 1  
    if has_lower:  # saw lowercase  
        points += 1  
  
    #Meeting the length requirement == True: +1 point  
    #Containing uppercase letters == True: +1 point  
    #Containing lowercase letters == True: +1 point  
    #Containing numbers == True: +1 point  
    #Containing special characters == True: +1 point  
  
    #if points == 1  
    if points == 1 or points == 2:  
        print("password is weak \n")  # say weak for 1 or 2  
        print(f"{points} point(s)")  
    #display password is medium  
    elif points == 3:  
        print("password is medium\n")  # 3 gets medium  
    #display password is good  
    elif points == 4:  
        print("password is good \n")  # 4 gets good  
    #display password is strong  
    elif points == 5:  
        print("password is strong \n")  # all 5, very strong  
    else:   
        print("please try again")  # no points, something went wrong  
  
    #loop repeats, can check another password  