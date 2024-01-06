def makePoints():
    n = int(input("enter number of points: "))
    for i in range(n):
        print("enter coordinates for point", i+1)
        points.append((int(input("enter x coordinate of point: " )), int(input("enter y coordinate of point: " ))))
    return points

def sortX(ps):
    l = ps.copy()
    for i in range(len(l)):
        for j in range(1,len(l)-i):
            if l[j][0]<l[j-1][0]:
                l[j],l[j-1] = l[j-1],l[j]
    return l

def sortY(ps):
    l = ps.copy()
    for i in range(len(l)):
        for j in range(1,len(l)-i):
            if l[j][1]>l[j-1][1]:
                l[j],l[j-1] = l[j-1],l[j]
    return l

def slope(px,py):
    try:
        m = (py[1]-px[1])/(py[0]-px[0])
    except:
        return 1
    return m
    
def ring(points):
    hull = []

    xL = sortX(points)
    yL = sortY(points)
    upoints = {'up': yL[0], 'down': yL[-1], 'right': xL[-1], 'left': xL[0]} #univeral points
    sp = upoints['up'] #top most point (subbordinate point)
    mp = upoints['left'] #left most point (main point)
    refp = upoints['up']
    m = slope(mp,sp) #slope b/w top most and left most points

    while True:
        for i in xL[::-1]:
            if i[0] in range(mp[0],sp[0]):
                if i[1]>=(i[0]*m+mp[1]) and i!=mp:
                    sp = i
                    m = slope(mp,sp)
        if mp not in hull:
            hull.append(mp)

        xL = sortX(points)
        yL = sortY(points)

        mp = sp
        if mp == upoints['up']:
            refp = upoints['right']
        if mp == upoints['right']:
            refp = upoints['down']
            break
        sp = refp

    sp = upoints['down']
    mp = upoints['right'] #right most point (main point)
    m = slope(mp,sp) #slope b/w bottom most and right most points

    while True:
        for i in xL[::-1]:
            if i[0] in range(sp[0], mp[0]):
                if i[1]<=(i[0]*m+sp[1]) and i!=mp:
                    sp = i
                    m = slope(sp,mp)
        if mp not in hull:
            hull.append(mp)
        xL = sortX(points)
        yL = sortY(points)
        mp = sp
        if mp == upoints['down']:
            refp = upoints['left']
        if mp == upoints['left']:
            break
        sp = refp
    return hull

def hull_area(points):
    Sum = 0
    for i in range(len(points)):
        try:
            Sum+=(points[i][0]*points[i+1][1]-points[i][1]*points[i+1][0])
        except:
            Sum+=(points[-1][0]*points[0][1]-points[-1][1]*points[0][0])

    return abs(Sum)

def convexHull(points):
    hull = ring(points)
    area = hull_area(hull)
    print(hull)
    return area

def area_checker(spoints):
    while len(spoints)>=3:
        area_dict = {}
        for i in range(1,len(spoints)+1):
            points = spoints[0:len(spoints)-i]+spoints[len(spoints)-i+1:len(spoints)]
            area_dict[spoints[len(spoints)-i]] = convexHull(points)
        x = min(area_dict, key=area_dict.get)
        spoints.remove(x)
        print(x)


spoints = [(1,0), (0,0), (0,1), (1,2), (2,1), (1,1)]
area_checker(spoints)
