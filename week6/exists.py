import os

def checkExistence(path: str):
    if os.path.exists(path):
        dir, file = os.path.split(path)
        print(dir, file)