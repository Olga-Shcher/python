#!/usr/bin/python3

from shutil import move
from pyrob.api import *


@task
def task_8_28():
    a=wall_is_on_the_left()#стена слева
    c=wall_is_on_the_right()#стена справа
    b=wall_is_above()#стена сверху
    d=wall_is_beneath()#стена снизу
    if b==True:
        while b==True:
            if a==False:#стена слева
                while b==True:
                    b=wall_is_above()#стена сверху
                    if b==False:
                        move_up()
                    else:
                        move_left()
                        a=wall_is_on_the_left()#стена слева
                        if a==True:
                            b=wall_is_above()#стена сверху
                            if b==False:
                                move_up()
                            else: 
                                while b==True:
                                    move_right()
                                    c=wall_is_on_the_right()
                                    b=wall_is_above()
            if c==False:
                while b==True:
                    b=wall_is_above()#стена сверху
                    if b==False:
                        move_up()
                    else:
                        move_right()
                        c=wall_is_on_the_right()#стена справа
                        if c==True:
                            b=wall_is_above()#стена сверху
                            if b==False:
                                move_up()
                            else: 
                                while b==True:
                                    move_left()
                                    a=wall_is_on_the_left()
                                    b=wall_is_above()
                    b=wall_is_above()
    if b==False:
        while b==False:
            move_up()
            b=wall_is_above()#стена сверху
        a=wall_is_on_the_left()
        if a==False:
            while a==False:
                move_left()
                a=wall_is_on_the_left()

            

if __name__ == '__main__':
    run_tasks()
