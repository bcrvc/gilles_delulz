# open inputfile/read/close 
with open('inputfile.txt') as f:
    lines = f.readlines()
 
for line in lines:
    if len(line) > 120:
        print line
