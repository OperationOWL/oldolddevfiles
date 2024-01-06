def binarysearch(l, x):
    mid,top,bottom = (len(l)//2, len(l), 0)
    count=0

    while l[mid]!=x:
        mid=(top+bottom)//2
        if count==len(l):
            return '-1'
        elif l[mid]<x:
            bottom=mid
        elif l[mid]>x:
            top=mid
        count+=1
    return mid


def bubblesort(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            print(l)
            if l[j]>=l[j+1]:
                l[j], l[j+1]=l[j+1], l[j]
    return l

def insertsort(l):
    for i in range(len(l)):
        key = l[i]
        for j in range(i, 0, -1):
            if l[j]>=key and l[j-1]<key:
                print(key, l[j])
                l.insert(j, l.pop(i))
    return l
            

l = [4,64,53,22,23,14,24,14]
print(bubblesort(l))
