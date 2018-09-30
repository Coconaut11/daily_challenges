#COMPLETED

from collections import namedtuple

data = "abcbabcc"

char_data = namedtuple("char_data", "seen idx")

def getResult(data, k):
    dic = {}
    lngest = "a"
    for i in range(0, len(data)):
        char = data[i]
        if char in dic:
            dic[char] = char_data(dic[char].seen + 1, dic[char].idx)
            subs = substring(data, dic[char].idx, i)
            if len(subs) == len(data):
                continue
            if dic[char].seen == k and len(subs) > len(lngest):
                lngest = subs
        else:
            dic[char] = char_data(1, i)
    return lngest      

def substring(s, i0, i1):
    s = s[i0 : i0 + i1-i0+1]
    return s

print(getResult(data, 3))
    