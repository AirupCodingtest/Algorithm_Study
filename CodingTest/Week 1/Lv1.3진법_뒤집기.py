def solution(n):
    a =[]
    b = 0
    sam = 1
    
    while(n>=1):
        a.append(int(n%3))
        n/=3
    for i in range(len(a)-1, -1, -1):
        b += a[i]*sam
        sam*=3
        
    return b