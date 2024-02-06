import turtle
n=int(input()) # количество крылышек 
a=2 #шаг черепахи для маленького кружечка 
turtle.shape("turtle")
turtle.left(90)
turtle.speed(10000)
def kolo(a): # 1 круг
    for i in range(120):
        turtle.forward(a)
        turtle.left(3)

def kolo2(a): # 2 круг
    for i in range(120):
        turtle.forward(a)
        turtle.right(3)

for i in range(n):
    kolo(a)
    kolo2(a)
    a+=0.25
