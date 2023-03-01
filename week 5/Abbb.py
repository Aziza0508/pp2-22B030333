import re

def task4(text):
    pattern = '[A-Z]{1}[a-z]+'
    x = re.findall(pattern, text)
    try:
        print(x)
    except AttributeError as e:
        print("Not found")

