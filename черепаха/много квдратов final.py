import turtle
turtle.shape('turtle')
a = 50  # сторона квадрата
while a<250:
    for i in range(4):
        turtle.forward(a)
        turtle.left(90)
    turtle.penup()
    turtle.backward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.pendown()
    a+=20
