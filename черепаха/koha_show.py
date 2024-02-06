import turtle

def koha(n,l):# l - довжина лінії, n - кількість ломаних ліній
        if n == 0:
            turtle.forward(l)
        else: 
            ln3 = l // 3
            koha(n-1,ln3)
            turtle.left(60)
            koha(n-1,ln3)
            turtle.right(120)
            koha(n-1,ln3)
            turtle.left(60)
            koha(n-1,ln3)    

def koha_show(n,l):
     for i in range(3): 
          koha(n,l)
          turtle.right(120)

koha_show(2,300)

    
    
    
    




