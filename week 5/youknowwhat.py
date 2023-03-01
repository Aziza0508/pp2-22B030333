import re

# If you don't i meant үтір точка и спэйс thingie

text = "a,d c.b"
def task6(text):
    pattern = '[,. ]'
    x = re.sub(pattern, ':', text)
    print(x)

print(task6(text))