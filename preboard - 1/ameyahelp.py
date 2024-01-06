import os
file = input('enter path of file: ')

def remove_word():
    f1=open(file, 'r')
    f2=open('temp', 'w')
    for i in f1.readlines():
        rec = i.split(' ')
        for j in rec:
            if len(j)!=4 and (len(j)!=6 and j[len(j)-1:len(j)]!='\n'):
                if j[len(j)-1:len(j)]!='\n':
                    f2.write(j+' ')
                else:
                    f2.write(j)
            elif (len(j)!=6 and j[len(j)-1:len(j)]!='\n'):
                f2.write('\n')
                
    f2.close()
    f1.close()
    os.remove(file)
    os.rename('temp', file)

def read():
    f = open(file, 'r')
    print(f.read())

remove_word()

while True:
    if input('enter y to read: ') == 'y':
        read()
    else:
        break
