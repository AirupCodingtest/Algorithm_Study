def solution(numLog):
    answer = ""
    a = len(numLog)
    i = 1
    while(a>i):
        if(numLog[i] - numLog[i-1] == 1):
            answer+="w"
        elif(numLog[i] - numLog[i-1] == -1):
            answer+="s"
        elif(numLog[i] - numLog[i-1] == 10):
            answer+="d"
        else:
            answer+="a"
        i+=1
        
    return answer