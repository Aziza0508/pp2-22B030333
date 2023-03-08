import os
import string

def generateFiles():
    for i in string.ascii_uppercase:
        open(f"{i}.txt", "x")

