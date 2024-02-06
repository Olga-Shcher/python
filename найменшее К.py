N=int(input())
k=0
while (2**k - N)<0:
    k+=1
else:
    print(k)