# JQ 1st maze generator
import turtle as t
import random as r
column = True
row = True
s = 50
t.Turtle()
t.shape("turtle")
t.color("white")
screen = t.Screen()
screen.bgcolor("black")
t.penup()
t.goto(-500,500)
t.forward(50)
t.pendown()
t.forward(500)
t.right(90)
t.forward(500)
t.right(90)
t.penup()
t.forward(50)
t.pendown()
t.forward(500)
t.right(90)
t.forward(500)
t.right(90)
t.penup()
t.forward(50)
t.pendown()
t.right(90)
t.penup()
counter = 0
t.goto(-500,450)
t.right(-90)
def rand_num():
    return r.randint(1,2)
t.speed(0)
while column == True:
    c1 = rand_num()
    c2 = rand_num()
    c3 = rand_num()
    c4 = rand_num()
    c5 = rand_num()
    c6 = rand_num()
    c7 = rand_num()
    c8 = rand_num()
    c9 = rand_num()
    c10 = rand_num()

    
   
    grid_columns = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
    for col in grid_columns:

        if t.xcor() >= 0:
            t.penup()
            t.right(180)
            t.forward(500)
            t.left(90)
            t.forward(50)
            t.left(90)
        if t.ycor() <= 0:
            column = False
        if col == 1:
            t.penup()
            t.forward(50)
            t.pendown()
            t.right(-90)
            t.forward(50)
            t.right(180)
            t.forward(50)
            t.right(-90)
            counter += 1
        elif col == 2:
            t.penup()
            t.forward(50)
            t.pendown()
            counter += 1
t.penup()
t.goto(-500,450)
t.pendown()
   

while row == True:
    l1 = r.randint(1,2)
    l2 = rand_num()
    l3 = rand_num()
    l4 = rand_num()
    l5 = rand_num()
    l6 = rand_num()
    l7 = rand_num()
    l8 = rand_num()
    l9 = rand_num()
    l10 = rand_num()
    grid_rows = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10]
    for row in grid_rows:

        if t.xcor() >= 0:
            t.penup()
            t.right(180)
            t.forward(500)
            t.left(90)
            t.forward(50)
            t.left(90)
        if t.ycor() <= 0:
            row = False
        if row == 1:
            t.penup()
            t.forward(50)
            t.pendown()
            t.right(-90)
            t.forward(50)
            t.right(180)
            t.forward(50)
            t.right(-90)
            counter += 1
        elif row == 2:
            t.penup()
            t.forward(50)
            t.pendown()
            counter += 1





t.done()


# go randomly inside until it touches a line then undo
