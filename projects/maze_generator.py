# JQ 1st maze generator
import turtle as t
import random as r
import time
column = True
row = False
row_list = [[],[],[],[],[],[],[],[],[],[]]
column_list = [[],[],[],[],[],[],[],[],[],[]]
r_sublist_index = 0
c_sublist_index = -3
s = 50
t.Turtle()
t.shape("turtle")
t.color("white")
screen = t.Screen()
screen.bgcolor("black")
#screen.tracer(0)
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
    row_list[r_sublist_index].append(c1)
    row_list[r_sublist_index].append(c2)
    row_list[r_sublist_index].append(c3)
    row_list[r_sublist_index].append(c4)
    row_list[r_sublist_index].append(c5)
    row_list[r_sublist_index].append(c6)
    row_list[r_sublist_index].append(c7)
    row_list[r_sublist_index].append(c8)
    row_list[r_sublist_index].append(c9)
    row_list[r_sublist_index].append(c10)
    r_sublist_index += 1
   
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
t.goto(-500,500)
t.speed(0)
t.pendown()
row = True
   
#
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
    column_list[c_sublist_index].append(l1)
    column_list[c_sublist_index].append(l2)
    column_list[c_sublist_index].append(l3)
    column_list[c_sublist_index].append(l4)
    column_list[c_sublist_index].append(l5)
    column_list[c_sublist_index].append(l6)
    column_list[c_sublist_index].append(l7)
    column_list[c_sublist_index].append(l8)
    column_list[c_sublist_index].append(l9)
    column_list[c_sublist_index].append(l10)
    c_sublist_index += 1
    grid_rows = [l1,l2,l3,l4,l5,l6,l7,l8,l9,]
    for rows in grid_rows:

        if t.ycor() <= 0:
            t.penup()
            t.setheading(90)
            t.forward(500)
            t.setheading(0)
            t.forward(50)
            t.setheading(270)
        if t.xcor() >= 0:
            row = False
        if rows == 1:
            t.setheading(270)
            t.penup()
            t.forward(50)
            if t.ycor() <= 0:
                t.penup()
                t.setheading(90)
                t.forward(500)
                t.setheading(0)
                t.forward(50)
                t.setheading(270)
            t.pendown()
            t.setheading(0)
            t.forward(50)
            t.right(180)
            t.forward(50)
            t.setheading(270)
            counter += 1
        elif rows == 2:
            t.setheading(270)
            t.penup()
            t.forward(50)
            if t.ycor() <= 0:
                t.penup()
                t.setheading(90)
                t.forward(500)
                t.setheading(0)
                t.forward(50)
                t.setheading(270)
            t.pendown()
            counter += 1


t.clear()

#screen.tracer(1)

   
    
t.done()


# go randomly inside until it touches a line then undo
