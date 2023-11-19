# 내 코드

def solution(n, control):
    for i in range(0, len(control)): 
        if control[i] == 'w':
            n += 1
        elif control[i] == 's':
            n -= 1
        elif control[i] == 'a':
            n -= 10
        elif control[i] == 'd':
            n += 10
    return n    
    

# 참고할만한 코드

'''
def solution(n, control):
    answer = n
    c = { 'w':1, 's':-1, 'a':-10, 'd':10 }
    for i in control:
        answer += c[i]
    return answer
'''

# 느낀 점

'''
1. if else 문으로 처리하지 말고 딕셔너리를 만들어서 처리해보자.
'''