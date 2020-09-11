import turtle

def CL(): #column
    for i in range(6):
        turtle.forward(300)
        turtle.backward(300)
        turtle.penup()
        turtle.left(90)
        turtle.forward(60)
        turtle.right(90)
        turtle.pendown()
def RW(): #raw
    for i in range(6):
        turtle.forward(300)
        turtle.backward(300)
        turtle.penup()
        turtle.right(90)
        turtle.forward(60)
        turtle.left(90)
        turtle.pendown()

def REP(): #reposition
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.left(90)

CL()
REP()
RW()
REP()
turtle.exitonclick()




