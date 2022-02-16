def solution(n):
    
    for i in range(1, n):
        rest = n%i
        if rest == 1 :
            break
        
    return i