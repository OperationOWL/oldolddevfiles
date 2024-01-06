import csv
import os

'''
This is a program to write into csv files.
It follows:
person - [pid, name, age]
'''

file = input('enter path of csv file: ')

def writeNew():
    f = open(file, 'w', newline = '')
    csv_w = csv.writer(f)
    while True:
        csv_w.writerow([int(input('enter id of person: ')), input('enter name of person: '), int(input('enter age of person: '))])
        if input('enter n to exit: ') == 'n':
            break
    print('erasing and re-writing file...\n')
    f.close()

def appendNew():
    f = open(file, 'a', newline = '')
    csv_w = csv.writer(f)
    while True:
        csv_w.writerow([int(input('enter id of person: ')), input('enter name of person: '), int(input('enter age of person: '))])
        if input('enter n to exit: ') == 'n':
            break
    print('\nwriting into file...\n')
    f.close()

def search(pid):
    print('searching...\n')
    f = open(file, 'r', newline = '')
    csv_r = csv.reader(f)
    for i in csv_r:
        if i[0] == pid:
            print(i)
    f.close()

def readFile():
    print('reading and displaying file...\n')
    f = open(file, 'r', newline = '')
    csv_r = csv.reader(f)
    for i in csv_r:
        print(i)
    print('\nend of file reached\n')
    f.close()

def update(Rowpid):
    print('searching...\n')
    f1 = open(file, 'r', newline = '')
    f2 = open('temp.csv', 'w', newline = '')
    csv_r = csv.reader(f1)
    csv_w = csv.writer(f2)
    print('updating...\n')
    for i in csv_r:
        if i[0] == pid:
            csv_w.writerow([int(input('enter id of new person: ')), input('enter name of new person: '), int(input('enter age of new person: '))])
        else:
            csv_r.writerow(i)
    f1.close()
    f2.close()
    os.remove(file)
    os.rename('temp.csv', file)
    print('\nupdated\n')


def deleteRow(pid):
    print('searching...\n')
    f1 = open(file, 'r', newline = '')
    f2 = open('temp.csv', 'w', newline = '')
    csv_r = csv.reader(f1)
    csv_w = csv.writer(f2)
    print('deleting...\n')
    for i in csv_r:
        if i[0] != pid:
            csv_w.writerow(i)
    f1.close()
    f2.close()
    os.remove(file)
    os.rename('temp.csv', file)
    print('deleted\n')

while True:
    choice = int(input('enter 1 to writeNew\nenter 2 to appendNew\nenter 3 to read\nenter 4 to search\nenter 5 to updateRow\nenter 6 to deleteRow\nenter 7 to exit\n'))
    if choice == 1:
        writeNew()
    if choice == 2:
        appendNew()
    if choice == 3:
        readFile()
    if choice == 4:
        search(input('enter pid to search: '))
    if choice == 5:
        updateRow(input('enter pid to update: '))
    if choice == 6:
        deleteRow(input('enter pid to delete: '))
    if choice == 7:
        break
