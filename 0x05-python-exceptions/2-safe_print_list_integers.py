#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    ans = 0
    while (i < x):
        try:
            print("{:d}".format(my_list[i]), end="")
            i += 1
            ans += 1
        except(TypeError):
            i += 1
        except(ValueError):
            i += 1
#       except(IndexError):
#           print()
#           return i
    print()
    return ans
