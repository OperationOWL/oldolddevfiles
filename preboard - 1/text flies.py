import os

'''
This is a program to write into csv files.
It follows:
person - [pid, name, age]
'''

file = input('enter path of text file: ')

def writeNew():
    f = open(file, 'w')
    f.write(input('enter what to write into file:\n '))
    print('\nerasing and re-writing file...\n')
    f.close()

def appendNew():
    f = open(file, 'a')
    f.write(input('enter what to write into file:\n '))
    print('\nwriting into file...\n')
    f.close()

def search(string):
    print('searching...\n')
    f = open(file, 'r')
    f.readlines()
    for i in f:
        rec = i.split('')
        for j in rec:
            if string == j:
                print(True)
                break
    f.close()

def readFile():
    print('reading and displaying file...\n')
    f = open(file, 'r', newline = '')
    print(f.read())
    print('\nend of file reached\n')
    f.close()

def updatestr(string):
    print('searching...\n')
    f1 = open(file, 'r')
    f2 = open('temp.txt', 'w')
    print('updating...\n')
    rec = f.read()
    rec = rec[0:rec.find(string)]+input('enter what to write: ')+rec[rec.find(string)+len(string):len(rec)]
    f2.write(rec)
    f1.close()
    f2.close()
    os.remove(file)
    os.rename('temp.txt', file)
    print('\nupdated\n')

 
def deletestr(string):
    print('searching...\n')
    f1 = open(file, 'r')
    f2 = open('temp.txt', 'w')
    print('updating...\n')
    rec = f1.read()
    rec = rec[0:rec.find(string)]+rec[rec.find(string)+len(string):len(rec)]
    f2.write(rec)
    f1.close()
    f2.close()
    os.remove(file)
    os.rename('temp.txt', file)
    print('\nupdated\n')

while True:
    choice = int(input('enter 1 to writeNew\nenter 2 to appendNew\nenter 3 to read\nenter 4 to search\nenter 5 to updateRow\nenter 6 to deleteRow\nenter 7 to exit\n'))
    if choice == 1:
        writeNew()
    if choice == 2:
        appendNew()
    if choice == 3:
        readFile()
    if choice == 4:
        search(input('enter sting to search: '))
    if choice == 5:
        updatestr(input('enter string to update: '))
    if choice == 6:
        deletestr(input('enter string to delete: '))
    if choice == 7:
        break
