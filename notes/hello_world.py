name= input("what is your name?").capitalize ()
print("hello", name)
print("welcome adventurer", name, " i need you to finish a quest for me")
answer= input("do you want to help me?").capitalize ()
if answer == "No":
    print("too bad")
elif answer == "Yes":
    print("follow me then")
else:
    print("print louder please")
    #crtl alt and down or up arow to select multiple lines