#!/usr/bin/python3

from multiprocessing.connection import wait
from pyrob.api import *


@task
def task_7_5():
    move_right()
    fill_cell()
    n=1
    c=wall_is_on_the_right()
    while c==False:
            for i in range(n):
                c=wall_is_on_the_right()
                if c==False:
                    move_right()
            c=wall_is_on_the_right()
            if c==False:
                fill_cell()
                n+=1



if __name__ == '__main__':
    run_tasks()
