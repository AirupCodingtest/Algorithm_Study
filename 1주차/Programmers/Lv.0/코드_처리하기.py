# 내 코드

def solution(code):
    mode = 0
    ret = ""
    for i in range(len(code)):
        if code[i] == "1":
            if mode == 0:
                mode = 1
            else:
                mode = 0
            continue

        if mode == 0 and i%2==0:
            ret += code[i]
            
        if mode == 1 and i%2==1:
            ret += code[i]
            
    if ret == "":
            return "EMPTY"    
    return ret


# 느낀 점
'''
1. 문제를 정확하게, 천천히, 제대로 읽자. 
'''            
        