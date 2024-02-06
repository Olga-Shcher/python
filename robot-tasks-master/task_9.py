#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    x=wall_is_on_the_right()#основная стена справа
    y=wall_is_above()#стена сверху
    z=wall_is_beneath()#стена снизу
    if x==False:
        while x==False:
            if y==False:
                fill_cell()
                move_right()
                x=wall_is_on_the_right()
                y=wall_is_above()
                z=wall_is_beneath()
            elif z==True and y==True:
                move_right()
                x=wall_is_on_the_right()
                y=wall_is_above()
                z=wall_is_beneath()
    if x==True and y==False:
        fill_cell()
             


if __name__ == '__main__':
    run_tasks()
