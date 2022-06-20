#!/usr/bin/python3
def safe_print_division(a, b):
    ans = None
    try:
        ans = a / b
    except(ZeroDivisionError):
        pass
    finally:
        print("{}".format(ans))
        return ans 
