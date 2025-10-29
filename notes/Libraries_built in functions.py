# JQ 1st Libraries And built in functions
import random
import turtle as t
colors = ["orange", "green","red","orange","purple","brown","pink","yellow"]
screen = t.Screen()
t.color(random.choice(colors))
t.shape("turtle")
t.speed(0)

t.fillcolor("blue")
t.begin_fill()
t.forward(250)
t.right(90)
t.forward(250)
t.right(90)
t.forward(250)
t.right(90)
t.forward(250)
t.right(90)
t.end_fill()

t.penup()
t.goto(50,50)

t.pendown()
t.color("red")

t.fillcolor("red")
t.begin_fill()
t.forward(250)
t.right(90)
t.forward(250)
t.right(90)
t.forward(250)
t.right(90)
t.forward(250)
t.right(90)
t.end_fill()
t.penup()
t.goto(100,100)

t.pendown()
t.color("green")
t.speed(10)
t.fillcolor("green")
t.shapesize(2)
t.title("kings man")
screen.tracer(0)
for x in range(1,1000):
    t.color(random.choice(colors))
    t.forward (x)
    t.right(20)
    t.color(random.choice(colors))
    t.width(20)
screen.tracer(1)

t.done()