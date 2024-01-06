import os
import pickle

file = input('enter file path: ')


def write():
    f = open(file ,'wb')
    while True:
        pickle.dump([int(input("enter id ")), input("enter name "), input("enter class ")],f)
        if input('enter n to break: ') == 'n':
            break
    f.close()

def read():
    f = open(file, 'rb')
    while True:
        try:
            print(pickle.load(f))
        except EOFError:
            break
    f.close()

def searchByID(pid):
    f = open(file, 'rb')
    while True:
        try:
            rec = pickle.load(f)
            if pid == rec[0]:
                print(rec)   
        except EOFError:
            break
    f.close()

def editByID(pid):
    f1 = open(file, 'rb')
    f2 = open('temp.bin', 'wb')
    while True:
        try:
            rec = pickle.load(f1)
            if pid != rec[0]:
                pickle.dump(rec, f2)
            else:
                pickle.dump([int(input('enter id: ')), input('enter name: '), input('enter age: ')], f2)
        except EOFError:
            break
    f1.close()
    f2.close()
    os.remove(file)
    os.rename('temp.bin', file)
    
def delByID(pid):
    f1 = open(file, 'rb')
    f2 = open('temp.bin', 'wb')
    while True:
        try:
            rec = pickle.load(f1)
            if pid != rec[0]:
                pickle.dump(rec, f2)
        except EOFError:
            break
    f1.close()
    f2.close()
    os.remove(file)
    os.rename('temp.bin', file)

while True:
    ch = int(input(" enter 1 for writing \n enter 2 for displaying \n enter 3 to search record by id \n enter 4 to edit by id \n enter 5 to delete by id \n enter 6 to break \n"))
    if ch==1:
        write()
    if ch==2:
        read()
    if ch==3:
        searchByID(int(input("enter id to search: ")))
    if ch == 4:
        editByID(int(input("enter id to edit ")))
    if ch == 5:
        delByID(int(input("enter id to delete ")))
    if ch==6:
        break
