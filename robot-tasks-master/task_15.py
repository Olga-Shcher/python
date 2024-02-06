#!/usr/bin/python3

from shutil import move
from pyrob.api import *


@task
def task_8_21():
    a=wall_is_on_the_left()#стена слева
    c=wall_is_on_the_right()#стена справа
    b=wall_is_above()#стена сверху
    d=wall_is_beneath()#стена снизу
    n=0#длина стенки
    if a==True:
            if d==True:#стена снизу
                while b==False:
                    move_up()
                    n+=1
                    b=wall_is_above()#стена сверху
                move_right(n)
            elif b==True:#стена сверху
                while d==False:
                    move_down()
                    n+=1
                    d=wall_is_beneath()#стена снизу
                move_right(n)
    elif c==True:
        if d==True:#стена снизу
                while b==False:
                    move_up()
                    n+=1
                    b=wall_is_above()#стена сверху
                move_left(n)
        elif b==True:#стена сверху
                while d==False:
                    move_down()
                    n+=1
                    d=wall_is_beneath()#стена снизу
                move_left(n)



     
    


if __name__ == '__main__':
    run_tasks()
