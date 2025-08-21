
import time
num = 0
for i in range (100):
    print(num)
    num = num +1
    time.sleep(0.01)


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
   # addition is done my putting print  and then the problen i parenthesis, no quotation marks
    print(2+2)
    #crtl alt and down or up arow to select multiple lines
   