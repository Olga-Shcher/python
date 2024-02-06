#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    n=0#счетчик закрашиваемых клеток
    c=wall_is_on_the_right()#проверка стены справа
    while n<=3 and c==False: 
            a=cell_is_filled() 
            if a==True: 
                n+=1 
                if n<3: 
                    move_right()
                    c=wall_is_on_the_right() 
            else:
                n=0 
                move_right() 
                c=wall_is_on_the_right()

if __name__ == '__main__':
    run_tasks()
