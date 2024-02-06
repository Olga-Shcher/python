def fibanachy(n):
    if n== 1 or n == 2: 
        return 1
    else:
        return fibanachy(n-1) + fibanachy(n-2)
    
n=int(input())
N=fibanachy(n)
print(N)