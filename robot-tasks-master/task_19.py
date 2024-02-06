#!/usr/bin/python3

from shutil import move
from pyrob.api import *


@task
def task_8_29():
    a=wall_is_on_the_left()#стена слева
    if a==False:
        while a==False:
            b=wall_is_above()#стена сверху
            d=wall_is_beneath()#стена снизу
            if b==True and d==True:
                    move_left()
                    a=wall_is_on_the_left()
            if b==False and d==False:
                a=1
    c=wall_is_on_the_right()
    b=wall_is_above()#стена сверху
    d=wall_is_beneath()#стена снизу              
    if c==False and a==True:
        while c==False:
            b=wall_is_above()#стена сверху
            d=wall_is_beneath()#стена снизу
            if b==True and d==True:
                    move_right()
                    c=wall_is_on_the_right()
            if b==False and d==False:
                c=1
    a=wall_is_on_the_left()#стена слева
    c=wall_is_on_the_right()#стена справа
    b=wall_is_above()#стена сверху
    d=wall_is_beneath()#стена снизу
    if b==False and d==False and (a==True or c==True):
        while b==False:
            move_up()
            b=wall_is_above()
        if c==True and b==True:
            move_left(10)

if __name__ == '__main__':
    run_tasks()
