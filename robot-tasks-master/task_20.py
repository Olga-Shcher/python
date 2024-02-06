#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    move_right()
    for i in range(6):
        fill_cell()
        for n in range(26):
            move_right()
            fill_cell()
        move_down()
        fill_cell()
        for x in range(26):
            move_left()
            fill_cell()
        move_down()



if __name__ == '__main__':
    run_tasks()
