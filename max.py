x=int(input())
max=0
while x!=0:
    if x>=max:
        max=x
    x=int(input()) 
if x==0:
    print(max)