import os

def copyContent(fromFile: str, toFile: str):
    with open(fromFile) as file1:
        data = file1.read()
    with open(toFile, "w") as file2:
        file2.write(data)