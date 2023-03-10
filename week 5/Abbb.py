import re

text = "Hello"
pattern = '[A-Z]{1}[a-z]+'
x = re.findall(pattern, text)
print(x)
