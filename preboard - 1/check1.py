file = 'test.txt'

f = open(file, 'r')

for i in f.readlines():
    for j in i.split(' '):
        if ((len(j)!=4 and j[len(j)-1:len(j)]!='\n') and (len(j)!=6 and j[len(j)-1:len(j)]!='\n')):
            print(j)

f.close()
