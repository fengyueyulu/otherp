import re

def get_word_frequencies(path):
    dic={}
    tx=open(path,"r").read().splitlines()

    for line in tx:
        line=re.sub(r"[,""/?.]","",line)
        line=re.sub(r'-','',line)
        for word in line.split():
            dic[word]=dic.get(word,0)+1
    print(dic)

get_word_frequencies("../text/text1")
