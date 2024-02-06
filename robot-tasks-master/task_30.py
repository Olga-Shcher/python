#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    c=wall_is_on_the_right()
    n=0
    while c==False: #узнаем количество сторон
        move_right()
        n+=1
        c=wall_is_on_the_right()
    while n>0:# идем по кругу пока и закрашиваем все треугольниками
        n-=2
        v=n+1
        move_down()
        for i in range(v):
            fill_cell()
            move_down()
        move_left()
        for i in range(v):
            fill_cell()
            move_left()
        move_up()
        for i in range(v):
            fill_cell()
            move_up()
        move_right()
        for i in range(v):
            fill_cell()
            move_right()
        move_down()
        move_left()
    a=wall_is_on_the_left()
    d=wall_is_beneath()
    while a!=True and d!=True:
        while a==False:
            move_left()
            a=wall_is_on_the_left()
        while d==False:
            move_down()
            d=wall_is_beneath()




    



if __name__ == '__main__':
    run_tasks()
