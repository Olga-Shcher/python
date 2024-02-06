def matryoshka(n):#мертва функція
    if n == 1: 
        print("Матрьошичка")
    else: 
        print("Вверх матрьошки n=", n)
        matryoshka(n-1)
        print("Низ матрьошки n=", n)

matryoshka(5) #виклик фукції