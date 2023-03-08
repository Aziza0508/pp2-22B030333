import os

def getNumberOfLines(path: str):
    with open(path) as file:
        print(len(file.readlines()))