"""Определите тип треугольника (остроугольный, тупоугольный, прямоугольный) с данными сторонами.
Необходимо вывести одно из слов: right для прямоугольного треугольника, acute для остроугольного треугольника,
obtuse для тупоугольного треугольника или impossible, треугольника с такими сторонами не существует.
"""
A=[]
N=3
max=0
for i in range(N):# масив
    x=int(input())
    A.append(x)
    if x >= max:
        max=x
A.remove(max)
if max * max > (A[0]*A[0])+ (A[1]*A[1]) and A[0]+A[1] > max:# тупокуктний
    print("obtuse")
elif max * max < (A[0]*A[0])+ (A[1]*A[1]): #гострокутний
    print("acute")
elif max * max == (A[0]*A[0])+ (A[1]*A[1]): #прямокутний
    print("right")
else:
    print("impossible")
