def multiplyList(data: list):
    res = 1
    for i in range(len(data)):
        res *= data[i]
    print(res)


multiplyList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])