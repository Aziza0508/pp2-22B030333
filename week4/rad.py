import math

# degrees to radians

def convertDegreeToRad(degree: int) -> float:
    return (degree * math.pi) / 180.0

userInput = int(input())
print(convertDegreeToRad(userInput))

