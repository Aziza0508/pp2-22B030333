import os


def writeListToFile(path: str, data: list):
    with open(path, "a") as file:
        file.writelines(data)

writeListToFile("input.txt", ["a", "b", "c"])
