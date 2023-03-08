import os

def deleteByPath(path: str):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("Such file does not exists")