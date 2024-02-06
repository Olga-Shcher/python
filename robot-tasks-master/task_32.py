#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    c=wall_is_on_the_right()
    x=0
    while c==False:
            b=wall_is_above()
            d=wall_is_beneath()
            a=cell_is_filled()#проверяем закрашена ли клетка
            if a==True: 
                x+=1
            if b==False and d==True:#проверяем стенку сверхy
                while b==False:
                    move_up()
                    b=wall_is_above()
                    d=wall_is_beneath()
                if d==False:
                    while d==False:
                        a=cell_is_filled()#проверяем закрашена ли клетка
                        if a==False:
                            fill_cell()
                        if a==True:
                            x+=1
                        move_down()
                        d=wall_is_beneath()
                if d==True:
                    move_right()
                    b=wall_is_above()
                    d=wall_is_beneath()
            if b==True and d==True:
                fill_cell()
                move_right()
                c=wall_is_on_the_right()
    if c==True: 
        mov('ax',x)
    

   
if __name__ == '__main__':
    run_tasks()

