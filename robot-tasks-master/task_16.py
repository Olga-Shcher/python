#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
    a=wall_is_above()#основная стена сверху
    n=0#длина буквы г
    if a==False:
        while a==False:#рисуем корпус буквы г
            move_up()
            a=wall_is_above()
    if a==True:
        b=wall_is_on_the_left()#стена cлева
        c=wall_is_on_the_right()
        if b==True:
            while c==False:#стена справа носика буквы г
                move_right()
                c=wall_is_on_the_right()
        elif b==False:
            while b==False:#стена слева носика буквы г
                move_left()
                b=wall_is_on_the_left()

if __name__ == '__main__':
    run_tasks()
