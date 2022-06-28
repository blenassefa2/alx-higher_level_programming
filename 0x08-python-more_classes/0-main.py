#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

myrectangle1 = Rectangle(8, 4) 
myrectangle2 = Rectangle(1, 8)

try: 
    print(myrectangle2 == Rectangle.bigger_or_equal('Rect', myrectangle1)) 
except Exception as e: 
    print("[{}] {}".format(e.__class__.__name__, e))