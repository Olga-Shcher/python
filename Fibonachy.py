"""
Числа трибоначчи - последовательность целых чисел {t n }, 
заданная с помощью рекуррентного соотношения: t 0 = 0, t 1 = 0, t 2 = 1 ,
t n+3 = t n + t n+1 + t n+2 Нужно найти номер первого числа трибоначчи, 
превосходящего заданное. Нумерация начинается с 0 .
"""
x = int(input())
A=[0,1,1]
i=2
y=0
while x >= A[i]:
    y=A[i]+ A[i-1] + A[i-2]
    A.append(y) 
    i+=1
if x == 0: 
    print(i)
else:
    print(i+1)