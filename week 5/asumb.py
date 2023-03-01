import re

def task5(text):
    pattern = 'a.?b$'
    x = re.findall(pattern, text)
    try:
        print(x)
    except AttributeError as e:
        print("Not found")