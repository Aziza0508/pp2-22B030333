import re

def task5(text):
    pattern = 'a.*b$'
    x = re.findall(pattern, text)
    print(x)
    
text = "ajcjkhb"
task5(text)
