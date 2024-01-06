def solution(data,n):
    l_out = []
    for i in data:
        if data.count(i)<=n:
            l_out.append(i)
    return l_out
print(solution([1,2,3,4], 1))