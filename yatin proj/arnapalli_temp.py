import pymysql

conn=pymysql.connect(host='localhost',user='root',password='1')
a=conn.cursor()
#a.execute('drop database project')
#a.execute('create database project')
a.execute('use  project')
#a.execute('create table student(rno int primary key,name varchar(20),marks decimal(5,2),address varchar(20))')
conn.commit()


while(True):
    print('1.insert')
    print('2.dispaly entire table')    
    print('3.search')
    print('4.update')
    print('5.delete')
    print('6. graph')
    print('7. Exit')
    ch=int(input('Enter ur choice'))
    if(ch==1):
        conn=pymysql.connect(host='localhost',user='root',password='1',database='project')
        a=conn.cursor()
        r=int(input('Enter roll number'))
        name=input('Enter name')
        m=float(input('Enter marks'))
        addr=input('Enter Address')
        x='insert into student values('+ str(r)+',"'+name+'"'+','+str(m)+',"'+addr+'"'+')'
        a.execute(x)
        print('one row inserted::')
        conn.commit()
    elif(ch==2):
        conn=pymysql.connect(host='localhost',user='root',password='1',database='project')
        a=conn.cursor()
        #r=int(input('Enter roll number to search::'))
        x='select *from student'
        a.execute(x)
        data=a.fetchall()
        for i in data:
            for j in i:
                print(j,end='\t')
            print()
        conn.commit()
    elif(ch==3):
        conn=pymysql.connect(host='localhost',user='root',password='1',database='project')
        a=conn.cursor()
        r=int(input('Enter roll number to search::'))
        x='select *from student where rno='+str(r)
        a.execute(x)
        data=a.fetchall()
        if(len(data)==0):
            print('roll number',r,'details not found')
        else:
            print(':::::::found::::::')
            print('Name=',data[0][1])
            print('Marks=',data[0][2])
            print('Address=',data[0][3])
        conn.commit()
    elif(ch==4):
         conn=pymysql.connect(host='localhost',user='root',password='1',database='project')
         a=conn.cursor()
         r=int(input('Enter roll number to update::'))
         x='select *from student where rno='+str(r)
         a.execute(x)
         data=a.fetchall()
         if(len(data)==0):
                print('roll number',r,'details not found')
         else:
                print(':::::::found::::::')
                print('Name=',data[0][1])
                print('Marks=',data[0][2])
                print('Address=',data[0][3])
         name=input('Enter new name:')
         marks=float(input('Enter new marks:'))
         addr=input('Enter new address:')
         x="update student set name='"+name+"',marks="+str(marks)+",address='"+addr+"' where  rno="+str(r)
         a.execute(x)
         print('row updates successfully')            
         conn.commit()


    elif(ch==5):
        pass
    elif(ch==6):
        import matplotlib.pyplot as plt
        L1=[]
        L2=[]
        conn=pymysql.connect(host='localhost',user='root',password='1',database='project')
        a=conn.cursor()
        x='select name,marks from student'
        a.execute(x)
        data=a.fetchall()
        for i in data:
            L1.append(i[0])
            L2.append(i[1])
        #print(L1)1
        #print(L2)
        plt.bar(L1,L2)
        plt.show()
        conn.commit()
    else:
        break


