#COMPLETE - This one was shitttt

import time

def caller(f, n):
    time.sleep(n/1000)
    f()

def func():
    print("Works :D")

caller(func, 1000)