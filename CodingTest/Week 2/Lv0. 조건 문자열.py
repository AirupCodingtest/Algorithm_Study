def solution(ineq, eq, a, b):
    if(ineq==">"and eq=="="):
        if(a>=b):
            return 1
        else:
            return 0
    elif(ineq=="<"and eq=="="):
        if(a<=b):
            return 1
        else:
            return 0
    elif(ineq==">"and eq=="!"):
        if(a>b):
            return 1
        else:
            return 0
    else:
        if(a<b):
            return 1
        else:
            return 0
        
    
    
    return answer