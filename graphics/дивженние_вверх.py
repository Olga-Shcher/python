import graphics as gr

SIZE_X = 400
SIZE_Y = 400

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)
coords = gr.Point(200, 200)
velocity = gr.Point(1, -2)


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)
    return new_point


#рисуем фон 1 раз
rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
rectangle.setFill('grey')
rectangle.draw(window)

#рисуем шарик 1 раз
circle = gr.Circle(coords, 10)
circle.setFill('red')
circle.draw(window)


while True:
    rectangle.move(0,0)
    circle.move(velocity.x,velocity.y)
    coords = add(coords, velocity)


