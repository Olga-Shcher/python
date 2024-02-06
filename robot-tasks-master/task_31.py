#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    a=wall_is_on_the_left()
    c=wall_is_on_the_right()
    d=wall_is_beneath()
    n=0 #если не будет выхода вниз 
    x=0#растояния между стенами
    if a==False:#left
        while a==False:
            move_left()
            a=wall_is_on_the_left()
            x+=1
    elif c==False:#right 
        while c==False: 
            move_right()
            c=wall_is_on_the_right()
            x+=1
    if n!=x:
        while n!=x:
            a=wall_is_on_the_left()
            c=wall_is_on_the_right()
            d=wall_is_beneath()
            if c==False:
                while d==True:
                    move_right()
                    n+=1
                    c=wall_is_on_the_right()
                    d=wall_is_beneath()
                    if c==True:
                        while d==True:
                                move_left()
                                d=wall_is_beneath()
                                a=wall_is_on_the_left()
                                n+=1
                                if a==True:
                                    return
            elif a==False: 
                while d==True:
                    move_left()
                    n+=1
                    a=wall_is_on_the_left()
                    d=wall_is_beneath()
                    if a==True: 
                        while d==True:
                            move_right()
                            d=wall_is_beneath()
                            n+=1
            if d==False: 
                move_down()
                n=0

    
    
    
    
    

    
    
     
     
     
     
     
       
       
       
       
       
       
       
       
        
        
                



if __name__ == '__main__':
    run_tasks()
