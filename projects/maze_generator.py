# JQ 1st maze generator   
import turtle as t    
import random as r  
# make maze_solvable False    
maze_solvable = False    
def is_maze_solvable(maze):    
    # 1 = wall, 2 = open path    
    visited = [[False for _ in range(10)] for _ in range(10)]    
    if maze[0][0] == 1 or maze[9][9] == 1:    
        return False    
    queue = [(0, 0)]    
    visited[0][0] = True    
    while queue:    
        x, y = queue.pop(0)    
        if (x, y) == (9, 9):    
            return True    
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:    
            nx, ny = x+dx, y+dy    
            if 0 <= nx < 10 and 0 <= ny < 10:    
                if not visited[nx][ny] and maze[nx][ny] == 2:    
                    visited[nx][ny] = True    
                    queue.append((nx, ny))    
    return False    

# While maze_solvable is False  
while maze_solvable == False:  
    # Make blank row_list with 10 lists  
    row_list = [[],[],[],[],[],[],[],[],[],[]]  
    # For i in range(10)  
    for i in range(10):  
        # For j in range(10)  
        for j in range(10):  
            # Add random 1 or 2 to row_list  
            row_list[i].append(r.randint(1,2))  
    # If is_maze_solvable(row_list) is True  
    if is_maze_solvable(row_list) == True:  
        # maze_solvable True  
        maze_solvable = True  
   
  
# draw maze with turtle    
# set turtle top left    
# for i in range(10)    
for i in range(10):    
    # for j in range(10)    
    for j in range(10):    
        # if its 1 draw white square    
        if row_list[i][j] == 1:    
            # draw filled square    
            pass    
        # else just move    
  
# make is_maze_solvable(maze)    
    # make visited grid 10x10 all False    
    # if maze[0][0] is 1 or maze[9][9] is 1 return False    
    # queue = (0,0)    
    # while queue not empty    
        # pop x,y from queue    
        # if x is 9 and y is 9 return True    
        # check all directions    
        # if next cell in bounds, not visited, and open, add to queue    
    # return False    
  


  
# Make maze_solvable False    
maze_solvable = False    
  
# While maze_solvable is False    
while maze_solvable == False:    
    # Make a blank row_list with 10 lists    
    row_list = [[],[],[],[],[],[],[],[],[],[]]    
    # For i in range(10):    
    for i in range(10):    
        # For j in range(10):    
        for j in range(10):    
            # Append random 1 or 2    
            row_list[i].append(r.randint(1,2))    
    # If maze is solvable    
    if is_maze_solvable(row_list):    
        maze_solvable = True    
  
# Draw maze with turtle    
t.Turtle()    
t.shape("turtle")    
t.color("white")    
screen = t.Screen()    
screen.bgcolor("black")    
t.speed(0)    
t.penup()    
t.goto(-500, 450)    
t.setheading(0)    
t.pendown()    
  
# For i in range(10):    
for i in range(10):    
    # For j in range(10):    
    for j in range(10):    
        t.penup()    
        t.goto(-500 + 50*j, 450 - 50*i)    
        # If row_list[i][j] == 1:    
        if row_list[i][j] == 1:    
            t.pendown()    
            t.fillcolor("white")    
            t.begin_fill()    
            for _ in range(4):    
                t.forward(50)    
                t.right(90)    
            t.end_fill()    
            t.penup()    
        # Else: just move, don't draw    
t.hideturtle()    
t.done()    
