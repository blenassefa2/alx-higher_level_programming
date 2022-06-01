#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
s = "Last digit of " +str(number) +" is "+str(last)+" and is "
if last > 5:
    print(s + "greater than 5")
elif last == 0:
    print(s + "0")
elif last < 6 and last > 0:
    print(s + "less than 6 and not 0")
