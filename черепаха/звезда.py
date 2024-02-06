import turtle
import math
n=int(input("Введите количество сторон "))
turtle.shape("turtle")
b=360/n
a=180-(180/n)
for i in range (n):
    turtle.right(a)
    turtle.forward(100)
