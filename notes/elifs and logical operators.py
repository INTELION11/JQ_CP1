# JQ 1st Elif and Logical Operators

grade = 100

if grade > 100:
    print(f"You did extra credit . .  you did {grade - 100}% extra credit ?")

elif grade == 100:
    print("Your grade is perfect")
else:
    print(f"Skill isue, L Bozo only getting {grade}")

username = "MsLaRose"
password = "1234"

user = input("enter is your username???")
pword = input("Enter your password")
if not user or not not pword:
    print("please actually write something")
elif user == "tia" and pword == "password":
    pass
    if pword == "password":
        print(" ")
    else:
        print("password incorrect")

elif user == username and pword == password:
    print("welcome Bozo")
elif user == username == username:
    print("password incorrect")
else:
    print("Incorrect credentials")  
    # and: True and True
    # or: true False
    # not : False
    #