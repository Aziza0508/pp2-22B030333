import math


# area of trapezoida 
def calcAreaOfTrap(height: int, firstBase: int, secondBase: int) -> float:
    return ((firstBase + secondBase) / 2) * height

h, base1 , base2 = [int(ele) for ele in input().split()]
print(calcAreaOfTrap(h, base1, base2))