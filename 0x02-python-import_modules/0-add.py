#!/usr/bin/python3
from add_0 import add


def my_func():
    a = 1
    b = 2
    print("%d + %d = %d" % (a, b, add(a, b)))


if __name__ == '__main__':
    my_func()
