import sys

f = open (sys.argv[1],'r')
file = f.readlines()
f.close()

file_write = open(sys.argv[1],'a')

for line in file:
    if "conforme a figura abaixo:" in line:
        print(line[line.find('conforme'):])

file_write.close()
