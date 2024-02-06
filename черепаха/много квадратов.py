import turtle
turtle.turtles
turtle.shape('turtle')
x = 10
while x >= 0:
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    x-=1

    