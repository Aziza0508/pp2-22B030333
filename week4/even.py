# Even

def getEvenUpUntil(until: int):
    num = 0
    while num <= until:
        yield num
        num += 2


userInput = int(input())

print(*[i for i in getEvenUpUntil(userInput)], sep = ",")