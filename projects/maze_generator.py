# JQ 1st maze generator
import turtle as t
import random as r

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

spaces = [[-300,300]]
r.randint(1,6)
# x coordinate and y coordinate
x = r.randint(1,5)
y = r.randint(1,5)
#size of the line


spaces.append([x,y])
t.done()


# go randomly inside until it touches a line then undo
