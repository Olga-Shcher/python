"""Функция принимает в качестве аргументов размерность пространства N и 2 вектора. 
Гарантируется, что размерности векторов совпадают. Векторы заданы списками длины N ."""

def dot_product(N,A:list,B:list):
    """Функция должна возвращать одно число -- 
    скалярное произведение заданных векторов."""
    s=0
    for i in range(N):
        s+=A[i] * B[i]
    return(s)


def test_dot(dot_product):
    print("testcase #1:", end="") 
    N=3
    A=[1,2,3]
    B=[1,2,3]
    print("YES" if dot_product(N,A,B) == 14 else "NO")

    
    print("testcase #2:", end="") 
    N=3
    A=[1,2,3]
    B=[4,5,6]
    print("YES" if dot_product(N,A,B) == 32 else "NO")

if __name__ == "__main__":
    test_dot(dot_product)