#!/usr/bin/python3

from multiprocessing.resource_sharer import stop
from pyrob.api import *


@task
def task_5_3():
    x=wall_is_beneath()
    z=True
    if x==False: # если нет стенки
        while x==False:
            move_right()
            x=wall_is_beneath()
    if x==True: #стенка появилась
        mov(x,z) # надо чтобы x оставался теперь постоянно тру)
        while x==True:
            z=wall_is_beneath()
            if z==True:
                while z==True:
                    move_right()
                    z=wall_is_beneath()
            else:
                x=2

        


if __name__ == '__main__':
    run_tasks()
