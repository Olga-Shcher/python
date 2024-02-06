import graphics as gr 
window=gr.GraphWin('Ukraine house', 500, 500)
def background():
    """ делаем фон 
    """
    sky=gr.Rectangle(gr.Point(0,0), gr.Point(500,250))
    sky.setFill('blue')
    earth=gr.Rectangle(gr.Point(0,250), gr.Point(500,500))
    earth.setFill('silver')
    earth.draw(window)
    sky.draw(window)

def circle(x,y,radius,color):
    #рисуем любой круг 
    circle=gr.Circle(gr.Point(x,y),radius)
    circle.setFill(color)
    circle.draw(window)

def Rectangle(x,y,z,f,color):
    #рисуем любой квадрат
    rectangle=gr.Rectangle(gr.Point(x,y),gr.Point(z,f))
    rectangle.setFill(color)
    rectangle.setOutline('black')
    rectangle.setWidth(3)
    rectangle.draw(window)

def triangle(x,y,z,f,d,color):
    #рисуем любой треугольник
    triangle=gr.Polygon(gr.Point(x,y),gr.Point(z,y),gr.Point(((x+z)/2),d))
    triangle.setFill(color)
    triangle.setOutline('black')
    triangle.setWidth(3)
    triangle.draw(window)

def cloud(x,y,radius,color):#тучка 
    for i in range (2):
        x+=20
        circle(x,y,radius,color)
    x-=50
    y+=10
    for i in range (3):
        x+=20
        circle(x,y,radius,color)

def dom(x,y,z,f,d,color):
    Rectangle(x,y,z,f,color)
    triangle(x,y,z,y,d,'red')
    Rectangle(x+55,y+55,z-55,f-55,'yellow')
    window_house(x,y,z,f,d,color)

def window_house(x,y,z,f,d,color):
    line_1=gr.Line(gr.Point(((x+55)+(z-55))/2, y+55),gr.Point(((x+55)+(z-55))/2, f-55))
    line_1.setOutline('black')
    line_1.setWidth(2) 
    line_1.draw(window)
    line_2=gr.Line(gr.Point(x+55,((y+55)+(f-55))/2),gr.Point(z-55,((y+55)+(f-55))/2))
    line_2.setOutline('black')
    line_2.setWidth(2)
    line_2.draw(window)

def tree(x,y,z,f,d):
    for i in range (3):
        triangle(x,y,z,f,d,"green")
        y-=20
        d-=20
    x=(x+z)/2-5
    z=x+10
    y+=60
    Rectangle(x,y,z,f,'brown')

background()
cloud(55,50,20,'white')
circle(400,50,40,'yellow')
dom(100,200,290,400,100,'grey')
tree(400,300,470,330,250)
window.getMouse()
window.close()