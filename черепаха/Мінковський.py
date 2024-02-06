import turtle

def min(n,l):# n- кількість ломаних, l - довжина відрізку 
    if n == 0: 
        turtle.forward(l)
    else: 
        l4=l/8
        min(n-1,l4)
        turtle.left(90)
        min(n-1,l4)
        turtle.right(90)
        min(n-1,l4)
        turtle.right(90)
        min(n-1,l4)
        min(n-1,l4)
        turtle.left(90)
        min(n-1,l4)
        turtle.left(90)
        min(n-1,l4)
        turtle.right(90)
        min(n-1,l4)



min(3,1000)
