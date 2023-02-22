import math

def calcAreaOfThePolygon(sides: int, length: int) -> float:
    apothem = length / (2 * math.tan(math.pi / sides))
    perimeter = sides * length
    area = 0.5 * apothem * perimeter
    return area

side, len = [int(ele) for ele in input().split()]
print(calcAreaOfThePolygon(side, len))

# something is so wrong here tho