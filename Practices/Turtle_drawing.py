import turtle as t
def draw_brach(lenghth):
    if lenghth > 5:
        for i in range(3):
            t.forward(lenghth)
            Draw_brach(lenghth / 3)
            t.backward(lenghth)
            t.right(60)

t.Turtle()
t.speed("fastest")
t.color("light blue")
t.penup()
t.goto(0,0)
t.pendown()


for i in range(6):
    draw_brach(100)
    t.right(60)

t.hideturtle()
t.done()