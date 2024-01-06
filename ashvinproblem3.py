#l1 = [10,10,20,30,40,40,50,60,60,70,80,100,100,200,200,400,600,800,1000,1000]
#l2 = [15,15,20,30,45,45,50,65,65,70,80,95,95,150,150,400,600,800,1200,1200]

#l1 = [5, 5, 7, 7]
#l2 = [4, 4, 1, 1]

l1 = [1, 1, 1, 1, 4, 4, 6]
l2 = [7, 7, 5, 5, 1, 1, 6]

l1.sort()
l2.sort()

Min = min(min(l1),min(l2))

try:
    ml = l1
    cl = l2
    pos = l1.index(Min)
except:
    ml = l2
    cl = l1
    pos = l2.index(Min)

for i in l1:
    try:
        l2.remove(i)
        l1.remove(i)
    except:
        pass

print(l1,l2)

print(int(Min*((len(l2)+len(l1))/2))-1)
