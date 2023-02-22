# Squares

def getSquaresUpUntil(until: int):

    num = 1
    while num <= until:
        yield num ** 2
        num += 1

for i in getSquaresUpUntil(5):
    print(i)
