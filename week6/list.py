import os

def scanPath(path: str, mode: int):
    dirs = [i for i in os.walk(path)]
    if mode == 0:
        for i in dirs:
            if len(i[1]) != 0:
                print(f"{i[0]}: {i[1]}")
    elif mode == 1:
        for i in dirs:
            print(i[0])
            print(f"{i[1]}: {i[2]}")
            print()
    elif mode == 2:
        for i in dirs:
            if len(i[2]) != 0:
                print(f"{i[0]}: {i[2]}")

