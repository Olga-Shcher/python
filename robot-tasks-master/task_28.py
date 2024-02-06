#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    n=0#количество закрашенных клеток 
    while n<5:
        c=cell_is_filled()#проверяем клетку на цвет
        if c==True:
            n+=1
            if n<5:
                move_right()
        else:
            move_right()


if __name__ == '__main__':
    run_tasks()
