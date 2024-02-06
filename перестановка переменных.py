#1 переменная


x = 2
y = 6
print("x =",x, "y =", y)
tmp = x
x = y
y = tmp
print("x =",x, "y =", y)


#через 2 переменные 

x = 7 
y = 8
print("x =",x, "y =", y)
tmp = x
tmp2 = y
x,y=y,x
print("x =",x, "y =", y)


