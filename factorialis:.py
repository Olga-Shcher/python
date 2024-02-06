def factorialis(n:int):
    if n == 1: 
        return n
    return n * factorialis(n-1)

n=7
print("Факторіал", n, "це", factorialis(n))