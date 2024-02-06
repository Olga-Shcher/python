"""Необходимо найти НОД двух чисел, используя алгоритм Евклида.
"""
a=int(input())
b=int(input())
while a != 0 and b != 0:
    if a > b: 
        a= a % b
    else:
        b= b % a
print(a+b)