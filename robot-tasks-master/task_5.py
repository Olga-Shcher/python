#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_2():
    x=True
    while x==True:
        x=wall_is_beneath()
        if x==True:
            move_right()
    


if __name__ == '__main__':
    run_tasks()
