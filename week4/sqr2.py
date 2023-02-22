# Get Squares from a to b

def getSquaresInRange(a: int, b: int):
    while a <= b:
        yield a ** 2
        a += 1

for i in getSquaresInRange(a=5, b=10):
    print(i)