import turtle
x= int(input())
turtle.shape("turtle")
turtle.speed(5)
for i in range(100):
    turtle.forward(x)
    turtle.left(90)
    x+=3
input()