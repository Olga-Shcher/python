#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    d=wall_is_beneath()#основная стена снизу, к которой мы будем идти
    n=0
    if d==False: 
        while d==False: 
            fill_cell()
            c=wall_is_on_the_right()
            while c==False:#идем вправо, пока не будет стены
                move_right()
                fill_cell()
                c=wall_is_on_the_right()
            n+=1
            d=wall_is_beneath()
            if d==False:
                move_down()          
                a=wall_is_on_the_left()
                fill_cell()
                while a==False:#идем влево, пока не будет стены
                    move_left()
                    fill_cell()
                    a=wall_is_on_the_left()
            d=wall_is_beneath()
            if d==False:
                move_down()    
    d=wall_is_beneath()
    c=wall_is_on_the_right()
    if d==True and c==True:
        a=wall_is_on_the_left()
        b=wall_is_above()
        if a==False and b==False:
            while a==False and b==False:
                move_left()
                a=wall_is_on_the_left()
        else:
            fill_cell()
            








        






if __name__ == '__main__':
    run_tasks()
