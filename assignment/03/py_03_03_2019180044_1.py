import turtle

def me():
    for i in range(4):
        turtle.forward(75)
        turtle.right(90)

turtle.penup()
turtle.goto(-300,300)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.goto(-350,250)
turtle.pendown()
turtle.forward(150)
turtle.penup()
turtle.goto(-275,200)
turtle.pendown()
turtle.right(180)
turtle.circle(50)
turtle.penup()
turtle.goto(-150,200)
turtle.left(90)
turtle.pendown()
turtle.forward(100)
turtle.backward(50)
turtle.left(90)
turtle.forward(50)
turtle.penup()

turtle.goto(-275,50)
turtle.pendown()
me()
turtle.penup()
turtle.goto(0,200)
turtle.pendown()
me()
turtle.penup()
turtle.forward(100)
turtle.right(90)
turtle.pendown()
turtle.forward(100)
turtle.penup()
turtle.goto(0,50)
turtle.pendown()
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.penup()

turtle.goto(200,200)
turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(75)
turtle.penup()
turtle.goto(200,100)
turtle.left(90)
turtle.pendown()
turtle.forward(120)
turtle.backward(100)
turtle.right(90)
turtle.forward(50)
turtle.backward(50)
turtle.left(90)
turtle.forward(80)
turtle.right(90)
turtle.forward(50)

turtle.exitonclick()

