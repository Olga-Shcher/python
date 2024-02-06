#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    n=1#длина коридора
    r=0#высота коридоров для закрашивания 
    c=wall_is_on_the_right()#ищем конец коридора
    move_right()
    if c==False:
        while c==False:
            n+=1#считаем длину коридора 
            b=wall_is_above()
            d=wall_is_beneath()
            if b==False:#проверяем стенку сверху
                while b==False:
                    move_up()
                    fill_cell()
                    r+=1
                    b=wall_is_above()
                move_down(r)
            if b==False:#проверяем стенку сверху
                while b==False:
                    move_down()
                    fill_cell()
                    r+=1
                    b=wall_is_beneath()
                    move_up(r)
            if b==True and d==True:
                move_right()
            r=0
            c=wall_is_on_the_right()
    c=wall_is_on_the_right()
    if c==True:
        b=wall_is_above()
        d=wall_is_beneath()
        if b==False:#проверяем стенку сверху
            while b==False:
                move_up()
                fill_cell()
                r+=1
                b=wall_is_above()
            move_down(r)
        if b==False:#проверяем стенку сверху
            while b==False:
                move_down()
                fill_cell()
                r+=1
                b=wall_is_beneath()
            move_up(r)
        if b==True and d==True:
            move_left(n)
if __name__ == '__main__':
    run_tasks()
