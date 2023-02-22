# devide by 3 and 4

def getDivNumbersUntil(until: int):
    num = 1
    while num <= until:
        if num % 3 == 0 and num % 4 == 0:
            yield num
        num += 1

userInput = int(input())
print(*[i for i in getDivNumbersUntil(userInput)], sep=",")