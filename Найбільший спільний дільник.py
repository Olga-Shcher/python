def gcd(a,b):
    if b == 0: 
        return a
    return gcd(b,a%b)

#2 версія
def gcd(a,b):
        return (a if b == 0 else gcd(b,a%b)) 

def step(a,n):
     return (1 if n == 0 else a * step(a,n-1))

def step_fast(a,n):
     if n == 0:
          return 1 
     elif n%2 == 1: #нечьотні
          return a * step_fast(a,n-1) 
     else:
         return step_fast(a**2, n//2)

a=4
n=4
b=21
print("Найбільший спільний дільник", a,"й", b, "це", gcd(a,b))
print (a, "в степені", n, "=", step_fast(a,n))