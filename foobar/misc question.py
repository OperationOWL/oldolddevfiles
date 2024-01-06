def fibonacci_sum(n):
    if n == 1:
        return 1
    a = 1
    b = 1
    count = 2
    sum = a+b
    while sum<=n:
        c = a + b
        a = b
        b = c
        sum+=c
        count+=1
    count-=1
    sum-=c
    return count

def square_sum(n):
    if n == 1:
        return 1
    count = 0
    sum = 0
    while sum<=n:
        sum+=2**count
        count+=1
    count-=1
    sum-=2**count
    return count

def solution(n):
    return fibonacci_sum(n)-square_sum(n)