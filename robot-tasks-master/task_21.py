#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    move_down()
    n=1
    d=wall_is_beneath()
    while d==False:
        for i in range(n):
            fill_cell()
            move_right()
        move_left(n)
        n+=1
        move_down()
        d=wall_is_beneath()



        
    





if __name__ == '__main__':
    run_tasks()
