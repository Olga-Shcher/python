
import turtle
turtle.turtles
turtle.shape('turtle')
x = 50
while x <=250:
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.penup()
    turtle.right(45)
    turtle.forward(20)
    turtle.left(45)
    turtle.pendown()
    x+=20

    