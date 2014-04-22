#!/usr/bin/python
file=open("out1.txt","r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
 
ls = [(k,v) for (k,v) in wordcount.items()]
 
ls.sort(key=lambda x:x[1],reverse=True)
 
for k,v in ls:
    print k, v
