#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_3():
    x=wall_is_on_the_right()#оснавная стена справа
    y=wall_is_above()# стена сверху
    z=wall_is_beneath()#стена снизу
    if x==False:
        while x==False:
            if y==True or z==True or (y==True or z==True):
                fill_cell()
                move_right()
                x=wall_is_on_the_right()
                y=wall_is_above()
                z=wall_is_beneath()
            else:
                move_right()
                x=wall_is_on_the_right()
                y=wall_is_above()
                z=wall_is_beneath()
    if x==True and y==True or z==True:
        fill_cell()

if __name__ == '__main__':
    run_tasks()
