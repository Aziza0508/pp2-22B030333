import re

# a and 0+ b's
text1 = "abbb"
text2 = "aaacd"
def task1(text):
    pattern = 'ab*'
    x = re.search(pattern, text)
    print(x.start())

print(task1(text1))
print(task1(text2))
