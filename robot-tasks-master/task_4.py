#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    x=wall_is_above()
    if x==False:
        move_up()
    else:
        x=wall_is_beneath()
        if x==False:
            move_down()
        else:
            x=wall_is_on_the_left()
            if x==False:
                move_left()
            else:
                move_right()

if __name__ == '__main__':
    run_tasks()
