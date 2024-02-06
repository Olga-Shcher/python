#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    x=cell_is_filled()#сначала проверяемся себя на предмет закрашивания
    r=True
    if x==False:
        while x==False:
            move_up()
            x=cell_is_filled()
    if x==True:
        mov(x,r)
        move_right()
        r=cell_is_filled()
        if r==False:
            move_left(2)




if __name__ == '__main__':
    run_tasks()
