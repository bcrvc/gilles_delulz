import re
 
# open the file to be formatted 
filename=open('sdstest.txt','r')
f=filename.read()
filename.close()
 
# put every sentence in a new line 
pat = ('(?<!Dr)(?<!Esq)\. +(?=[A-Z])')
lines = re.sub(pat,'.\n',f)
print lines 
 
# write the formatted text into a new txt file 
filename = open("out.txt", "w")
filename.write(lines)
filename.close()
