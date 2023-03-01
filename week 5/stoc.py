import re

def task7(text):
    x = re.split('_', text)

    res = x[0]
    for i in range(1, len(x)):
        res += x[i].capitalize()
    print(res)

text = "snake_to_camel"
print(task7(text))