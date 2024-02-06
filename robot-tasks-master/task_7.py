#!/usr/bin/python3

from shutil import move
from pyrob.api import *


@task
def task_5_4():
    z=True
    a=0
    x=wall_is_beneath()
    while x==False: #спускаемся вниз пока не наткнемся на стенку
        move_down()
        x=wall_is_beneath()
    if x==True:
        mov(x,z)
        while x==True:
            z=wall_is_beneath()
            if z==True:
                while z==True:
                    move_right()
                    z=wall_is_beneath()
                    a+=1 #длина стены
            else:
                move_down()
                move_left(a)
                x=2
    


if __name__ == '__main__':
    run_tasks()
