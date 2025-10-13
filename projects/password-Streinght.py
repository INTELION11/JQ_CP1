#JQ 1st Paasword streinth
#password is ask "what is your password"
#points = 0
password = input("what is your password \n")
points = 0
#length = len(password)
length = len(password)
#list special_character
special_character = list("!@#$%^&*()_+-=[]{|;:,}.<>?)")
#list numbers
numbers = list("1234567890")
#characters is list(password)
characters = list(password)
#loop for letter in characters
for letter in characters:
#    special is bool([special_character].find(letter))
    special = bool((letter).find[special_character])
#    num is bool([numbers].find(letter))
    num = bool((letter).find[numbers])
#    upperc is bool(password isupper.)
    upperc = letter .isupper()
#    lowerc is bool(password islower.)
    lowerc =  letter .islower()
#    if special is true then spec_points += 1
    if special == True:
        spec_points += 1
    else: 
        print(" ")
#    if num is true then num_points += 1
    if num == True:
        num_points += 1
    else: 
        print(" ")
#    if upperc is true then upper_points += 1
    if upperc == True:
        upperc_points += 1
    else: 
        print(" ")
#    if lowerc is true then lower_points += 1
    if lowerc == True:
        lowerc_points += 1
    else: 
        print(" ")
#if special >= 1 then points += 1
if special >= 1:
#if num >= 1 then points += 1

#if upperc >= 1 then points += 1

#if lowerc >= 1 then points += 1
#if length >= 8 then points += 1



#Meeting the length requirement == True: +1 point
#Containing uppercase letters == True: +1 point
#Containing lowercase letters == True: +1 point
#Containing numbers == True: +1 point
#Containing special characters == True: +1 point

#if points == 1
#display password is weak
#if points == 2
#display password is weak
#if points == 3
#display password is medium
#if points == 4
#display password is good
#if points == 5
#display password is strong
#else display please try again