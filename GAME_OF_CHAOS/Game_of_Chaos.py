from random import randint
import turtle
import time

# Three fixed nodes of the triangle.
R = 300
x1 = 0
y1 = R
x2 = -R
y2 = -R
x3 = R
y3 = -R
x0 = randint(-299, 299)
y0 = randint(-299, 299)


def start_position(x1, y1, x2, y2, x3, y3):
    global x0
    global y0
    a = (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
    b = (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
    c = (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)
    while not ((a >= 0 and b >= 0 and c >= 0) or (a <= 0 and b <= 0 and c <= 0)):
        x0 = randint(-299, 299)
        y0 = randint(-299, 299)
        a = (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
        b = (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
        c = (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)
    print(x0, y0)


print(start_position(x1, y1, x2, y2, x3, y3))

# Initializing screen
turtle.TurtleScreen._RUNNING = True
myScreen = turtle.Screen()
myScreen.setup(width=1.0, height=1.0)

# Initializing pen
myPen = turtle.Turtle()

# Draw the three fixed nodes and start node
myPen.penup()
myPen.goto(x1, y1)
myPen.dot()
myPen.goto(x2, y2)
myPen.dot()
myPen.goto(x3, y3)
myPen.dot()
myPen.goto(x0, y0)
myPen.dot()

# Drawing process
step = 40000
turtle.speed("fastest")
turtle.tracer(0, 0)
while (step):
    turtle.speed(10000000)
    rand_num = randint(1, 3)
    print(rand_num)
    if rand_num == 1:
        x0 = (x0 + x1) // 2
        y0 = (y1 + y0) // 2
    elif rand_num == 2:
        x0 = (x2 + x0) // 2
        y0 = (y2 + y0) // 2
    else:
        x0 = (x3 + x0) // 2
        y0 = (y3 + y0) // 2
    myPen.goto(x0, y0)
    myPen.dot()
    step -= 1

turtle.update()
print("The end!!")
myScreen.exitonclick()
