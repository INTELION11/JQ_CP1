# JQ 1st User Sign In
while True:
    name_input = input("What is your username? \n")
    pass_input =  input ("What is your password? \n")
    userpass = name_input + pass_input

    if userpass == "JacobQuezada":
        print(f"welcome Senpai kun")

    elif userpass != "JacobQuezada":
        if name_input != "Jacob":
            print (" Username is Incorrect, senpai ")

        elif pass_input != "Quezada":
            print("Password Is Incorrect, bro ")
        else:
            print(" There was an error processing your data")
    else:
            print("There was a problem processing your data")