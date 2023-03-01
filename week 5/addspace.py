import re

#split
def task9(text):
    pattern = '[A-Z][^A-Z]*'
    x = re.findall(pattern, text)
    for i in x:
        print(i + " ", end = '')

text = "AmericanDreamOrNot?"
print(task9(text))