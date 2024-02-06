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

def triangle(x,y,z,d,color):
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

def dom(x,y,z,f,d,color):#x,y = 1 точка квадрата, z,f = 2 точка квадрта(вниз вправо по диагонали), d = точка криши по y
    Rectangle(x,y,z,f,color)
    triangle(x,y,z,d,'red')
    Rectangle(x+55,y+55,z-55,f-55,'yellow')
    window_house(x,y,z,f)

def window_house(x,y,z,f):
    line_1=gr.Line(gr.Point(((x+55)+(z-55))/2, y+55),gr.Point(((x+55)+(z-55))/2, f-55))
    line_1.setOutline('black')
    line_1.setWidth(2) 
    line_1.draw(window)
    line_2=gr.Line(gr.Point(x+55,((y+55)+(f-55))/2),gr.Point(z-55,((y+55)+(f-55))/2))
    line_2.setOutline('black')
    line_2.setWidth(2)
    line_2.draw(window)

def tree(x,y,z,d,f):
    Rectangle((x+z)/2-(z-x)/8,y,(x+z)/2+(z-x)/8,f,'brown')
    for i in range (4):
        triangle(x,y,z,d,"green")
        y=(d+y)/2
        d+=d-y

background()
circle(60,50,40,'yellow')
cloud(10,70,15,'white')
cloud(50,71,15,'white')
cloud(400,30,17,'white')
cloud(250,100,14,'white')
dom(300,180,360,250,140,'grey')
tree(20,310,100,260,330)
tree(150,400,250,340,420)
tree(430,270,490,235,285)

window.getMouse()
window.close()