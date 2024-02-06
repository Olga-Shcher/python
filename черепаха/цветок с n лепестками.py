n=int(input()) #количество лепестков
b=360/n
import turtle
turtle.shape("turtle")
turtle.speed(10)
def kolo():
    for i in range(180):
        turtle.forward(2)
        turtle.left(2)
def kolo2():
    for i in range(180):
        turtle.forward(2)
        turtle.right(2)
for i in range(n//2):
    kolo()
    kolo2()
    turtle.left(b)