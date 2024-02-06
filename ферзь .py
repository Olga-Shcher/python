a,b,c,d,=int(input()),int(input()),int(input()),int(input())
if a==c or b==d or (a==b and c==d) or (a-c==d-b) or (c-a==d-b):
    print("YES")
else:
    print("NO")