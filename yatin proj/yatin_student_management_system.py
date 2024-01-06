import pymysql
import matplotlib.pyplot as plt

mycon=pymysql.connect(host='localhost',user='root',password='1')
cursor=mycon.cursor()
cursor.execute('use project')
mycon.commit()

while(True):

    print('1. insert')
    print('2. display entire table')    
    print('3. search')
    print('4. update')
    print('5. delete')
    print('6. graph')
    print('7. Exit')
    ch=int(input("Enter your choice: "))

    if(ch==1):
        cursor=mycon.cursor()
        cursor.execute(f'insert into student values({str(int(input('Enter roll number:')))},{input('Enter name:')},{str(float(input('Enter marks:')))},{input('Enter address:')})')
        print('one row inserted')
        mycon.commit()

    elif(ch==2):
        cursor=mycon.cursor()
        x='select * from student'
        cursor.execute(x)
        data=cursor.fetchall()
        for i in data:
            for j in i:
                print(j,end='\t')
            print('')
        mycon.commit()

    elif(ch==3):
        cursor=mycon.cursor()
        cursor.execute(f'select * from student where rno = {str(int(input('Enter roll number to search: ')))}')
        data=cursor.fetchall()
        if(len(data)==0):
            print('details not found')
        else:
            print('found')
            print('Name: ', data[0][1])
            print('Marks: ', data[0][2])
            print('addressess: ', data[0][3])
        mycon.commit()

    elif(ch==4):
         cursor=mycon.cursor()
         r=int(input('Enter roll number to update: '))
         cursor.execute(f'select * from student where rno {str(r)}')
         data=cursor.fetchall()
         if(len(data)==0):
            print('roll number details not found')
         cursor.execute(f'update student set name = input('Enter name:')}, marks = {str(float(input('Enter marks:')))}, address = {input('Enter address:')}) where rno={r}')
         print('row updated successfully')
         mycon.commit()

    elif(ch==5):
        print('delete could not be initiatied')

    elif(ch==6):
        names=[]
        names=[]
        cursor=mycon.cursor()
        cursor.execute('select name,marks from student')
        data=cursor.fetchall()
        for i in data:
            names.append(i[0])
            marks.append(i[1])
        plt.bar(names,marks)
        plt.show()
        mycon.commit()
    elif ch==7:
        break

    else:
        print('enter choice from 1-7 only.')
        continue
