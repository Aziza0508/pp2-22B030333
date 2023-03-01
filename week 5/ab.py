import re
import string

# ЗАЧЕЕЕЕЕЕМ НУЖЕН ИМПОРТ СТРИНГ????

# a and 0+ b's
text1 = "abbb"
text2 = "aaacd"
def task1(text):
    pattern = 'ab*'
    x = re.search(pattern, text)
    print(x.start())

print(task1(text1))
print(task1(text2))


def task2(text):
    pattern = 'ab{2,3}'
    x = re.findall(pattern, text)
    try:
        print(x)
    except AttributeError as e:
        print("Not found")


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


def task4(text):
    pattern = '[A-Z]{1}[a-z]+'
    x = re.findall(pattern, text)
    try:
        print(x)
    except AttributeError as e:
        print("Not found")


def task5(text):
    pattern = 'a.?b$'
    x = re.findall(pattern, text)
    try:
        print(x)
    except AttributeError as e:
        print("Not found")


def task6(text):
    pattern = '[,. ]'
    x = re.sub(pattern, ':', text)
    print(x)


def task7(text):
    x = re.split('_', text)

    res = x[0]
    for i in range(1, len(x)):
        res += x[i].capitalize()
    print(res)


def task8(text):
    pattern = '[A-Z]'
    x = re.split(pattern, text)
    print(x)


def task9(text):
    pattern = '[A-Z][^A-Z]*'
    x = re.findall(pattern, text)
    for i in x:
        print(i + " ", end='')


def task10(text):
    pattern = '[A-Z][^A-Z]*'
    x = re.findall(pattern, text)
    res = ""
    for i in x:
        res += i.lower() + "_"
    print(res[0:len(res) - 1])