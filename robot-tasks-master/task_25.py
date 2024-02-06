#!/usr/bin/python3

from shutil import move
from pyrob.api import *


@task
def task_2_2():    
    move_right()
    c=wall_is_on_the_right()
    while c==False:
        for i in range(3):
            move_down()
            fill_cell()
        move_up()
        move_right()
        c=wall_is_on_the_right()
        if c==False:
            move_right()
            for i in range(3):
                move_left()
                fill_cell()
            move_up()
            move_right(5)
            move_up()
        if c==True:
            fill_cell()
            for i in range(2):
                move_left()
                fill_cell()
            move_up()
        


if __name__ == '__main__':
    run_tasks()
