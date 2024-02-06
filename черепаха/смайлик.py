import turtle
turtle.shape("turtle")

def kolo():
    turtle.goto(0,0)
    turtle.circle(100)

def eys():
    turtle.penup()
    turtle.goto(-50,120)
    turtle.pendown()
    turtle.begin_fill() #Необходимо вызвать перед рисованием фигуры, которую надо закрасить
    turtle.filling() # красить
    turtle.circle(15)
    turtle.color("blue") # установка цвета
    turtle.end_fill() #Вызвать после окончания рисования фигуры 
    turtle.color("black")
    turtle.penup()
    turtle.goto(50,120)
    turtle.pendown()
    turtle.begin_fill() #Необходимо вызвать перед рисованием фигуры, которую надо закрасить
    turtle.filling() # красить
    turtle.circle(15)
    turtle.color("blue") # установка цвета
    turtle.end_fill() #Вызвать после окончания рисования фигуры 
    turtle.color("black")

def nouse():
    turtle.penup()
    turtle.goto(0,80)
    turtle.pendown()
    turtle.pensize(15)	
    turtle.right(90)
    turtle.forward(20)
    turtle.pensize(0)


def smile():
    turtle.penup()
    turtle.goto(50,60)
    turtle.pendown()
    turtle.pensize(10)
    turtle.color("red")
    turtle.circle(-50,180)


turtle.begin_fill() #Необходимо вызвать перед рисованием фигуры, которую надо закрасить
turtle.filling() # красить
kolo()
turtle.color("yellow") # установка цвета
turtle.end_fill() #Вызвать после окончания рисования фигуры 
turtle.color("black")

eys()

nouse()
smile()