import re

# a + bb/bbb

text1 = "abbb"
text2 = "aaab"

def task2(text):
    pattern = 'ab{2,3}'
    x = re.findall(pattern, text)
    try:
        print(x)
    except AttributeError as e:
        print("Not found")

print(task2(text1))
print(task2(text2))