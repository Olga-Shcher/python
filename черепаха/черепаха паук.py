import turtle 
n= int(input())
turtle.shape("turtle")
x=360/n # градусы ножек паука 
while n > 0: 
    turtle.forward(50)
    turtle.stamp()
    turtle.backward(50)
    turtle.right(x)
    n-=1
input()
