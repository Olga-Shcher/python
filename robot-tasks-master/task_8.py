#!/usr/bin/python3

from tkinter import Y
from pyrob.api import *


@task
def task_5_7():
    
    x=wall_is_above()
    y=wall_is_beneath()
    if x==True or y==True:
        while x==True or y==True:
            move_right()
            x=wall_is_above()
            y=wall_is_beneath()



if __name__ == '__main__':
    run_tasks()
