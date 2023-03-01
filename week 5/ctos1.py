import re



def task10(text):
    pattern = '[A-Z][^A-Z]*'
    pattern1 = "[^A-Z]"
    # poidee tut ne ochen' pravilno but i am so tired
       
    x = re.findall(pattern, text)
    y = re.findall(pattern1, text)

    res = ""
    for i in y:
        res += y[0] + "_"
    
    for i in range (1, len(x)):
        res += i.lower() + "_"
    print(res[0:len(res) - 1])


text = "CamelToYouKnowWhat"
# works only when camel starts with capital letter
print(task10(text))