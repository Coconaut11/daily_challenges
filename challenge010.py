#COMPLETE - This one was shitttt

import time

def caller(f, n):
    time.sleep(n/1000)
    f()

def func():
    print("Works :D")

caller(func, 1)
caller(func, 2000)
caller(func, 1000)
caller(func, 500)
caller(func, 250)
caller(func, 175)
caller(func, 175/2)
caller(func, 175/4)
caller(func, 175/8)
caller(func, 175/16)
caller(func, 175/32)
caller(func, 175/64)
caller(func, 175/128)
caller(func, 175/256)
caller(func, 175/(256*2))
