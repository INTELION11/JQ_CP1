# JQ 1st maze generator
import turtle as t
import random as r
column = True
row = False
s = 50
t.Turtle()
t.shape("turtle")
t.color("white")
screen = t.Screen()
screen.bgcolor("black")
t.penup()
t.goto(-300,300)
t.forward(50)
t.pendown()
t.forward(250)
t.right(90)
t.forward(300)
t.right(90)
t.penup()
t.forward(50)
t.pendown()
t.forward(250)
t.right(90)
t.forward(300)
t.right(90)
t.penup()
t.forward(50)
t.pendown()
t.right(90)
t.penup()
counter = 0
t.goto(-300,250)
t.right(-90)
def rand_num():
    return r.randint(1,2)

while column == True:
    c1 = rand_num()
    c2 = rand_num()
    c3 = rand_num()
    c4 = rand_num()
    c5 = rand_num()
    c6 = rand_num()
    
    
    grid_columns = [c1,c2,c3,c4,c5,c6]
    for col in grid_columns:
        if col == 1:
            t.penup()
            t.forward(50)
            t.pendown()
            t.right(-90)
            t.forward(50)
            t.right(180)
            t.forward(50)
            t.right(-90)
        else:
            t.penup()
            t.forward(50)
            t.pendown()
        if t.xcor() == 0:
            t.right(180)
            t.forward(250)
            t.right(-90)
            t.forward(50)
            t.right(-90)
        else:
            print("something went wrong")

   

while row == True:
    l1 = r.randint(1,2)
    l2 = rand_num()
    l3 = rand_num()
    l4 = rand_num()
    l5 = rand_num()
    l6 = rand_num()
    grid_rows = [l1,l2,l3,l4,l5,l6]
    row = False


t.done()


# go randomly inside until it touches a line then undo
