import re



def task10(text):
    pattern = '[A-Z][a-z]*' 
    # poidee tut ne ochen' pravilno but i am so tired
    # for i in range (1, len(x)):
    #    
    x = re.findall(pattern, text)
    res = ""
    for i in x:
        res += i.lower() + "_"
    print(res[0:len(res) - 1])

text = "CamelToYouKnowWhat"
# works only when camel starts with capital letter
print(task10(text))

#well i tried
