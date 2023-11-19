def solution(code):
    answer = ""
    mode = -1
    for i in range(len(code)):
        if code[i] == "1" :
            mode *= -1
        if mode != 1 and code[i]!="1" :
            if i%2==0  :
                answer += code[i]
        if mode == 1 :
            if i%2==1 and code[i]!="1"  :
                answer += code[i]
    if answer == "":
        return "EMPTY"
    return answer