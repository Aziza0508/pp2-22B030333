import re
import string

def task3(text):
    pattern = '_'
    x = re.split(pattern, text)
    # splitting the given text by underscore
    try:
        result = []
        # iterating through the list and combining them together. Not including the last one
        for i in range(len(x) - 1):
            if x[i] != '' and x[i + 1] != '' and x[i] in string.ascii_lowercase and x[i + 1] in string.ascii_lowercase:
                result.append(f"{x[i]}_{x[i + 1]}")
        print(result)
    except AttributeError as e:
        print("Not found")