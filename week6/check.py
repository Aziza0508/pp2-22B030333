import os

def checkAccess(path: str):
    if os.path.exists(path):
        print(f"Existence: {os.access(path, os.F_OK)}")
        print(f"Readability: {os.access(path, os.R_OK)}")
        print(f"Writability: {os.access(path, os.W_OK)}")
        print(f"Executability: {os.access(path, os.X_OK)}")
    else:
        print("File does not exist")

