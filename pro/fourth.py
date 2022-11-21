import operator
import re

def get_word_frequencies(path):
    dic={}
    tx=open(path,"r").read().splitlines()

    for line in tx:
        line=re.sub(r"[,""/?.]","",line)
        line=re.sub(r'-','',line)
        for word in line.split():
            dic[word]=dic.get(word,0)+1
    sorted_tuples = sorted(dic.items(), key=operator.itemgetter(1),reverse=True)
    dic={k:v for k,v in sorted_tuples}
    print(dic)

get_word_frequencies("../text/text1")
