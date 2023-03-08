import time
import math

def calcSquareIn(num: int, timeout: int):
    time.sleep(timeout / 1000)
    print(math.sqrt(num))

calcSquareIn(25100, 2123)