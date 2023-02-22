# Count down from b to 0
def countDownFromB(a: int):
    while 0 <= a:
        yield a
        a -= 1
print(*[i for i in countDownFromB(8)], sep=", ")