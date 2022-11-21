import re

def isChinese(word):
    for ch in word:
        if  '\u4e00'<=ch<='\u9fff':
            return True
        return  False

with open ('../text/filtered_words',encoding='utf-8') as fp:
    text=fp.read()
    text=text.split("\n")
    inp=input("请输入：")
    for t in text:
        if re.findall(t,inp):
            for item in re.findall(t,inp):
                if isChinese(item):
                    inp=re.sub(t,"*"*len(t),inp)
                else:
                    inp=re.sub(t,"*",inp)
    print(inp)
