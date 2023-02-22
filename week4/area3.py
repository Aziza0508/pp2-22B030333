import math

def calcAreaOfTheParallelogram(height: int, length: int):
    return length * height

side, len = [int(ele) for ele in input().split()]
print(calcAreaOfTheParallelogram(side, len))
