# подключение библиотеки под синонимом gr
import graphics as gr

# Инициализация окна с названием "Russian game" и размером 100х100 пикселей
window = gr.GraphWin("Russian game", 300, 300)

# Создание круга с радиусом 10 и координатами центра (50, 50)
my_circle = gr.Circle(gr.Point(50, 50), 10)

# Создание отрезка с концами в точках (2, 4) и (4, 8)
my_line = gr.Line(gr.Point(2, 4), gr.Point(4, 8))

# Создание прямоугольника у которого диагональ — отрезок с концами в точках (2, 4) и (4, 8)
my_rectangle = gr.Rectangle(gr.Point(2, 4), gr.Point(4, 8))

#Метод move передвигает обьект circle на (1, 1) относительно его текущего положения
my_circle.move(1, 1)

# Отрисовка примитивов в окне window
my_circle.draw(window)
my_line.draw(window)
my_rectangle.draw(window)
 
#  Ожидание нажатия кнопки мыши по окну.
window.getMouse()
# Закрытие окна после завершения работы с графикой
window.close()

