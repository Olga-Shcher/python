
"""x y координати точок, 
r радіус круга з центром в початку координат"""
def dot(A):
    x,y,r=input().split() 
    #The split() method splits a string into a list. перетворюємо те що отримали в список, але без пробілів
    x,y,r=int(x),int(y),int(r) #переводимо з str в числа, щоб можна було працювати
    print("YES" if x**2 + y**2 <= r**2  else "NO")


def test_dot(dot):
    print("testcase #1:", end="") 
    x,y,r=-1,3,1
    print("YES" if x**2 + y**2 <= r**2 else "NO")

    
    print("testcase #2:", end="")
    x,y,r=2,2,4
    print("YES" if x**2 + y**2 <= r**2 else "NO")

    
    print("testcase #3:", end="")
    x,y,r=-3,-5,2
    print("YES" if x**2 + y**2 <= r**2 else "NO")


    print("testcase #4:", end="")
    x,y,r=2,-7,7
    print("YES" if x**2 + y**2 <= r**2 else "NO")


    print("testcase #5:", end="")
    x,y,r=2,-7,8
    print("YES" if x**2 + y**2 <= r**2 else "NO")


    print("testcase #6:", end="")
    x,y,r=1000000,1000000,1000000
    print("YES" if x**2 + y**2 <= r**2 else "NO")


test_dot(dot)