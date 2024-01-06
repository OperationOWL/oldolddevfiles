#l = eval(input('enter list of elements: '))
'''
def radius(l):
    if len(l)==1:
        return [-1,-1]
    s = 0
    for i in range(1,len(l)):
        if i%2==1:
            s+=l[i]-l[i-1]
        else:
            s+=l[i-1]-l[i]

    if s<=0:
        return [-1,-1]

    if i%2==0:
        return [s*2,1] #odd
    else:            #even
        if s*2/3-int(s*2/3) == 0:
            return [s*2//3,1]
        else:
            return [s*2,3]
'''
'''

    if len(pegs)%2==1:
        i=1
    else:
        i=0
'''


def radius(pegs):
    s=0
    for i in range(len(pegs)-1):
        if i%2==0:
            dist = pegs[i+1]-pegs[i]
        else:
            dist = pegs[i]-pegs[i+1]
        s+=dist

    if s<0:
        return [-1,-1]

    if len(pegs)%2==0:
        if s*2/3-s*2//3 == 0:
            return [s*2//3,1]
        else:
            return [s*2,3]
    elif len(pegs)%2==1:
        return [s*2,1]

def solution(pegs):
    if len(pegs)<2:
        return [-1,-1]
    r_list =  radius(pegs)
    if r_list == [-1,-1]:
        return [-1,-1]

    r = r_list[0]/r_list[1]

    for i in range(len(pegs)-1):
        d=pegs[i+1]-pegs[i]
        if d-r<1:
            return [-1,-1]
        r = d-r
    if r<1:
        return [-1,-1]
    else:
        return r_list
print(solution([4, 30, 50]))  # [12, 1]
print(solution([4, 17, 50]))  # [-1, -1]
print(solution([1, 51]))  # [100, 3]
print(solution([1]))  # [-1, -1]
print(solution([1, 31]))  # [20, 1]
print(solution([1, 31, 51, 71]))  # [20, 1]
print(solution([1, 31, 51, 71, 91]))  # [20, 1]
print(solution([4, 9, 17, 31, 40]))  # [4, 1] )
