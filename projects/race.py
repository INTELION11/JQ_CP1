# JQ 1st  turrtle race
import turtle as t
import random
#race is true
race = True
#summon turtles 1-5 t1 = t.Turtle()
t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle()
t4 = t.Turtle()
t5 = t.Turtle()
t6 = t.Turtle()
#change screen color to black
screen = t.Screen()
screen.bgcolor("black")

#make turtles 1-5 turtle shapes t.shape("turtle")
t1.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")
t4.shape("turtle")
t5.shape("turtle")
t6.shape("turtle")


t1.color("green")
t2.color("blue")
t3.color("red")
t4.color("brown")
t5.color("orange")
t1.width(3)
t2.width(3)
t3.width(3)
t4.width(3)
t5.width(3)
t6.width(5)


t6.speed(5)
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



t6.speed(.5)
t6.penup()
t6.goto(500,550)
t6.pendown()
t6.right(90)
t6.color("white")
t6.forward(1200)
t6.right(270)
t6.forward(50)
t6.right(270)
t6.forward(1200)
t6.penup()
t6.goto(500,75)
t6.right(270)
t6.pendown()
t6.forward(1100)
t6.right(90)
t6.forward(50)
t6.right(90)
t6.forward(1100)
t6.right(-90)
t6.forward(50)
t6.right(-90)
t6.forward(1100)
t6.right(90)
t6.forward(50)
t6.right(90)
t6.forward(1100)
t6.right(-90)
t6.forward(50)
t6.right(-90)
t6.forward(1100)
t6.right(-90)
t6.forward(250)
t6.right(-90)
t6.forward(1150)
t6.right(-90)
t6.forward(250)
t6.right(-90)
t6.forward(1100)




while race == True:
    t1.forward(random.randint(5,30))
    t2.forward(random.randint(5,30))
    t3.forward(random.randint(5,30))
    t4.forward(random.randint(5,30))
    t5.forward(random.randint(5,30))
    if t1.pos() >= (500,50):
        print("")
        winner = "Green"
        race = False
        
    if t2.pos() >= (500,100):
        print("")
        winner = "Blue"
        race = False
        
    if t3.pos() >= (500,150):
        print("")
        winner = "Red"
        race = False
        
    if t4.pos() >= (500,200):
        print("")
        winner = "Brown"
        race = False
        
    if t5.pos() >= (500,250):
        print("")
        winner = "Orange"
        race = False
        
t6.write(f"The {winner} Turtle Wins!",font=("Arial",50,"normal"))


t.done()
if winner == "Green":
    print("Green turtle has won!")
elif winner == "Blue":
    print("blue turtle has won!")
elif winner == "Red":
    print("red turtle has won!")
elif winner == "Brown":
    print("brown turtle has won!")
elif winner == "Orange":
    print("orange turtle has won!")
else: 
    print("there was an error")