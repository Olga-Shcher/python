import graphics as gr 

window = gr.GraphWin ("Ukraine game", 700,700)
alpha = 0.2
def tractal_rectangle(a,b,c,d, deep=10):# deep це глибина рекурсії, максимальна кількість дій 
    if deep < 1: 
        return
    for m,n in (a,b) , (b,c) , (c,d) , (d,a): #перебираємо з 2 параметрами 
        gr.Line(gr.Point(*m),gr.Point(*n)).draw(window) #*a це виклик заготовленних параметрів, тобто там очікується х і y для того щоб поставити точку, а можно скоротити й використати тільки *
    """gr.Line(gr.Point(*a),gr.Point(*b)).draw(window) 
    gr.Line(gr.Point(*b),gr.Point(*c)).draw(window)
    gr.Line(gr.Point(*c),gr.Point(*d)).draw(window)
    gr.Line(gr.Point(*d),gr.Point(*a)).draw(window"""
    a1 = (a[0]*(1-alpha)+ b[0]*alpha, a[1]*(1-alpha)+ b[1]*alpha)
    b1 = (b[0]*(1-alpha)+ c[0]*alpha, b[1]*(1-alpha)+ c[1]*alpha)
    c1 = (c[0]*(1-alpha)+ d[0]*alpha, c[1]*(1-alpha)+ d[1]*alpha)
    d1 = (d[0]*(1-alpha)+ a[0]*alpha, d[1]*(1-alpha)+ a[1]*alpha)
    tractal_rectangle(a1,b1,c1,d1,deep-1)

tractal_rectangle((100,100), (500,100), (500,500), (100,500))
my_rectangle = gr.Rectangle(gr.Point(2,4), gr.Point(4,8))
my_rectangle.draw(window)# малюємо 
