import turtle
n=int(input()) #количество дуг
turtle.shape("turtle")
turtle.speed(500)
turtle.left(90)
def duga_Big():
    for i in range(180):
        turtle.forward(1)
        turtle.right(1)

def duga_small():
    for i in range(180):
        turtle.forward(0.225)
        turtle.right(1)

for i in range(n):
    duga_Big()
    duga_small()