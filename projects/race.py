# JQ 1st  turrtle race
import turtle as t
import random
race = True
t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle()
t4 = t.Turtle()
t5 = t.Turtle()
t6 = t.Turtle()
t1.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")
t4.shape("turtle")
t5.shape("turtle")
t1.color("green")
t2.color("blue")
t3.color("red")
t4.color("brown")
t5.color("orange")
t1.penup()
t1.goto(-500,50)
t1.pendown()
t2.penup()
t2.goto(-500,100)
t2.pendown()
t3.penup()
t3.goto(-500,150)
t3.pendown()
t4.penup()
t4.goto(-500,200)
t4.pendown()
t5.penup()
t5.goto(-500,250)
t5.pendown()
t6.penup()
t6.goto(500,550)
t6.pendown()
t6.right(90)
t6.color("black")
t6.forward(1000)
while race == True:
    t1.forward(random.randint(1,100))
    t2.forward(random.randint(1,100))
    t3.forward(random.randint(1,100))
    t4.forward(random.randint(1,100))
    t5.forward(random.randint(1,100))
    if t1.pos() >= (500,50):
        print("turtle 1 has won!")
        winner = "t1"
        race = False
        
    if t2.pos() >= (500,100):
        print("turtle 1 has won!")
        winner = "t2"
        race = False
        
    if t3.pos() >= (500,150):
        print("turtle 1 has won!")
        winner = "t3"
        race = False
        
    if t4.pos() >= (500,200):
        print("turtle 1 has won!")
        winner = "t4"
        race = False
        
    if t5.pos() >= (500,250):
        print("turtle 1 has won!")
        winner = "t5"
        race = False
        

    


t.done()
if winner == "t1":
    print("Green turtle has won!")
elif winner == "t2":
    print("Green turtle has won!")
elif winner == "t3":
    print("Green turtle has won!")
elif winner == "t4":
    print("Green turtle has won!")
elif winner == "t5":
    print("Green turtle has won!")
else: 
    print("there was an error")