    #JQ 1st Paasword streinth
    #password is ask "what is your password"
    #points = 0
while True:
    password = input("what is your password \n").strip()
    points = 0
    num_points = 0
    spec_points = 0
    upperc_points = 0
    lowerc_points = 0


    #length = len(password)
    length = len(password)
    #list special_character
    special_character = ("!@#$%^&*()_+-=[]{|;:,}.<>?)")
    #list numbers
    numbers = ("1234567890")
    #characters is list(password)
    characters = (password)
    #loop for letter in characters


    for i in characters:
        numb = i.isdigit()
        if numb:
            points = points + 1
            print("Your password contains a number character! +1 point")
            break
        else: continue



    for i in characters:
    #    special is bool([special_character].find(letter))
        special = bool((i).find(special_character))
    #    num is bool([numbers].find(letter))
        num = bool((i).find(numbers))
    #    upperc is bool(password isupper.)
        upperc = i .isupper()
    #    lowerc is bool(password islower.)
        lowerc =  i .islower()
    #    if special is true then spec_points += 1
        if special == True:
            spec_points += 1
        else: 
            print("")
    #    if num is true then num_points += 1
        if num == True:
            num_points += 1
        else: 
            print("")
    #    if upperc is true then upper_points += 1
        if upperc == True:
            upperc_points += 1
        else: 
            print("")
    #    if lowerc is true then lower_points += 1
        if lowerc == True:
            lowerc_points += 1
        else: 
            print("")
    #if special >= 1 then points += 1
    if special >= 1:
        points += 1
    else:
        Points = points
    #if num >= 1 then points += 1
    if num >= 1:
        points += 1
    else:
        Points = points
    #if upperc >= 1 then points += 1
    if upperc >= 1:
        points += 1
    else:
        Points = points
    #if lowerc >= 1 then points += 1
    if lowerc >= 1:
        points += 1
    else:
        Points = points
    #if length >= 8 then points += 1
    if length >= 8:
        points += 1
    else:
        Points = points


    #Meeting the length requirement == True: +1 point
    #Containing uppercase letters == True: +1 point
    #Containing lowercase letters == True: +1 point
    #Containing numbers == True: +1 point
    #Containing special characters == True: +1 point

    #if points == 1
    if points == 1:
        print("password is weak \n")
        print("1 point")
    #display password is weak
    #if points == 2
    elif points == 2:
        print("password is weak \n")
        print("2 points")
    #display password is weak
    #if points == 3
    elif points == 3:
        print("password is medium\n")
    #display password is medium
    #if points == 4
    elif points == 4:
        print("password is good \n")
    #display password is good
    #if points == 5
    elif points == 5:
        print("password is strong \n")
    else: 
        print("please try again")
    #display password is strong
    #else display please try again