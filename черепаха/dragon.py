import turtle
def dr(n,l,s=1):# s — показник, для відрезкалення фігури по осі Y 
    if n == 0: 
        turtle.forward(l)
    else:
        l2=l/2
        turtle.right(45*s)
        dr(n-1,l2,1)
        turtle.left(90*s)
        dr(n-1,l2,-1)#зеркалимо малюнок, робимо по осі y 
        turtle.right(45*s)
dr(5,200)