#!/usr/bin/python3

from operator import truediv
from pyrob.api import *


@task
def task_3_1():
    x=wall_is_on_the_right()
    while x==False:
        move_right()
        x=wall_is_on_the_right()



if __name__ == '__main__':
    run_tasks()
