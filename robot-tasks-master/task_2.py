#!/usr/bin/python3

from re import A
from pyrob.api import *


@task


def task_1_2():
    def n1(a):
        for i in range(1):
            move_right(2)
            move_down(a)
    n1(a=2)
    fill_cell()
    n1(a=1)


if __name__ == '__main__':
    run_tasks()
