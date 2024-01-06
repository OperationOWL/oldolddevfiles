#l1 = [10,10,20,30,40,40,50,60,60,70,80,100,100,200,200,400,600,800,1000,1200]
#l2 = [15,15,20,30,45,45,50,65,65,70,80,95,95,150,150,400,600,800,1000,1200]
l1 = [7,7,6,6]
l2 = [2,2,3,3]

l1_copy = l1.copy()
l2_copy = l2.copy()

l1.sort()
l2.sort()
l4 = []
cost = 0
i=0

l3 = l1+l2

Min = min(l3)
while True:
    try:
        l3.remove(Min)
    except:
        break

Min2 = min(l3)


while i in range(len(l1)):
    if l1[i] in l2:
        l2.remove(l1[i])
        l1.remove(l1[i])
        i-=1
    i+=1

l3 = l1+l2
l3.sort()


for i in l3:
    if i<Min*2:
        l4.append(i)
    elif i>=Min*2:
        cost+=Min/2

l4.sort()


cost += (sum(l4[0:len(l4)//2])//2)-Min*2

cost+=min(Min*2,Min2)


print(cost)
