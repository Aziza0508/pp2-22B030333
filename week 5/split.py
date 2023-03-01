import re

def task8(text):
    pattern = '[A-Z]'
    x = re.split(pattern, text)
    print(x)

text = "americanDreamOrNot?"
print(task8(text))
# pretend that this code works