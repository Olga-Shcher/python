x=int(input())
y=0
while x!=0:
    if x%2==0:
        y+=1
    x=int(input())
if x==0:
    print(y)