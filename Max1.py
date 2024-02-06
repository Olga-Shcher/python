def max1(N,x):
    """Вводится последовательность, состоящая только из 0 и 1. 
    Необходимо найти максимальное количество 1, идущих подряд (без 0 между ними).
    """
    # A=[0]*N #робимо пустий масив
    # n=0
    max=0
    w=0
    # while n < N: #заповнюємо його
        # x=int(input())
        # A[n]=x
        # A[n]=x[n]
        # n+=1
    for i in x:# проходимось по масиву й знаходимо кількість 
        if x[i] == 1:
            w+=1
        if w > max:
            max+=1
        if x[i] == 0:
            w=0
    print(max)
    return(max)





def Test_case():
    print("testcase #1:", end="")
    a=0
    N=1
    x=[0]
    print("Ok" if  max1(N,x) == a else "Fail")
 
    print("testcase #2:", end="")
    a=2
    N=5
    x=[1,0,1,1,0]
    print("Ok" if  max1(N,x) == a else "Fail")

    # print("testcase #3:", end="")
    # a=
    # N=
    # x=
    # print("Ok" if  max1(N,x) == a else "Fail")
    # 
    # print("testcase #4:", end="")
    # a=
    # N=
    # x=
    # print("Ok" if  max1(N,x) == a else "Fail")

    # print("testcase #5:", end="") 
    # a=
    # N=
    # x=
    # print("Ok" if  max1(N,x) == a else "Fail")


    # print("testcase #6:", end="")  
    # a=
    # N=
    # x=
    # print("Ok" if  max1(N,x) == a else "Fail")



if __name__ == '__main__':
    Test_case()
 