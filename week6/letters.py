
def calcLetters(data: str):
    upper = 0
    lower = 0
    for i in range(len(data)):
        if 65 <= ord(data[i]) <= 90:
            upper += 1
        elif 97 <= ord(data[i]) <= 122:
            lower += 1
    print(upper, lower)

calcLetters("Hello")