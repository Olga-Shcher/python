x=int(input())
y=int(input())
max=0
z=0
while y!=0:
    if y==max:
        z+=1
    elif y>x:
        max=y 
        z=1
    x=max
    y=int(input())

if y==0:
    print(z)