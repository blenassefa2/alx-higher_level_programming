#!/usr/bin/python3
from add_0 import add


def my_func():
    a = 1
    b = 2
    print(f"{a:d} + {b:d} = {add(a, b):d}")


if __name__ == '__main__':
    my_func()
