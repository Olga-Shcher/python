import turtle
def levi(n,l):
    if n==0: 
        turtle.forward(l)
    else:
        l2=l/2
        turtle.left(45)
        levi(n-1,l2)
        turtle.right(45)
        turtle.right(45)
        levi(n-1,l2)
        turtle.left(45)

levi(5,200)

