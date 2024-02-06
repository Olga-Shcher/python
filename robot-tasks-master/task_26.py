#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    d=wall_is_beneath()#стенка внизу, основная
    if d==False:
        while d==False:
            c=wall_is_on_the_right()#проверяем стенку справа
            if c==False:
                while c==False:
                    move_right()
                    fill_cell()
                    for i in range(2):
                        move_down()
                        fill_cell()
                    move_up()
                    move_right()
                    c=wall_is_on_the_right()
                    if c==False:
                        fill_cell()
                        for i in range(2):
                            move_left()
                            fill_cell()
                        move_up()
                        move_right(4)
                        c=wall_is_on_the_right()
                        d=wall_is_beneath()
                    if c==True:#если есть стенка справа спускаемся вниз 
                        fill_cell()
                        for i in range(2):
                            move_left()
                            fill_cell()
                        move_down()
                        d=wall_is_beneath()
                        a=wall_is_on_the_left()
                        if d==False:
                            while d==False and a==False:
                                move_down(2)
                                a=wall_is_on_the_left()
                                if a==False:
                                    while a==False:
                                        move_right()
                                        fill_cell()
                                        for i in range(2):
                                            move_down()
                                            fill_cell()
                                        move_up()
                                        move_right()
                                        fill_cell()
                                        for i in range(2):
                                            move_left()
                                            fill_cell()
                                        move_up()
                                        a=wall_is_on_the_left()
                                        if a==False:
                                            move_left(4)
                                        if a==True:
                                            move_down()
                                            d=wall_is_beneath()
                                            if d==False:
                                                move_down(3)
                                                d=wall_is_beneath()
                                                c=wall_is_on_the_right()          
                        if d==True:
                            move_left(36)
                            move_up(2)                   



                    




    


if __name__ == '__main__':
    run_tasks()
