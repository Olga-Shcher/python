import turtle
turtle.shape("turtle") 
x = 0.01
turtle.speed(100)
for i in range(500):
    turtle.forward(x)
    x += 0.02
    turtle.left(10)

