#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
    x=wall_is_on_the_right()#оснавная стена справа
    y=wall_is_above()# стена сверху
    z=wall_is_beneath()#стена снизу
    if x==False:
        while x==False:
            y=wall_is_above()
            if y==False:# стена сверху
                move_up()
                fill_cell()
                move_down()
                z=wall_is_beneath()
                if z==False:#стена снизу
                    move_down()
                    fill_cell()
                    move_up()
                    move_right()
                    x=wall_is_on_the_right()
                    y=wall_is_above()
                    z=wall_is_beneath()
                else:
                    move_right()
                    x=wall_is_on_the_right()
                    y=wall_is_above()
                    z=wall_is_beneath()
            elif y==True and z==True:
                fill_cell()
                move_right()
                x=wall_is_on_the_right()
                y=wall_is_above()
                z=wall_is_beneath()
            else:
                    move_down()
                    fill_cell()
                    move_up()
                    move_right()
                    x=wall_is_on_the_right()
                    y=wall_is_above()
                    z=wall_is_beneath()
    if x==True:
        if y==False:
            move_up()
            fill_cell()
            move_down()
            if z==False:
                move_down()
                fill_cell()
                move_up()
        if y==True:
            if z==False:
                move_down()
                fill_cell()
                move_up()
            elif z==True:
                fill_cell()
        


if __name__ == '__main__':
    run_tasks()
