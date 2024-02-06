N=int(input())
A=[]
F=[0]*100
max=0
r=0
for i in range(N):
    x=int(input())
    F[x]+=1
for k in range(100):
    if F[k] > max:
        max=F[k]
        r=k
print(r)
