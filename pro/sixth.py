import operator
import re
import glob
dict={}

def word_split_count():
    global dict
    gl=glob.glob("../text/*")
    for path in gl:
        fp=open(path,'r').read().splitlines()
        for lines in fp:
            lines = re.sub(r"[/,.""?]", "", lines)
            lines = re.sub(r"-","",lines)
            for word in lines.split():
                dict[word]=dict.get(word,0)+1

    sorted_tuples = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
    dict = {k: v for k, v in sorted_tuples}

if __name__=="__main__":
    word_split_count()
    print(dict)