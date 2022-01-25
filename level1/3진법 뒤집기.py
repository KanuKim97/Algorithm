def solution(n):
    answer = 0
    rest = []
    tmp = 0
    
    while n > 0:
        n, mod = divmod(n, 3)
        rest.append(mod)
    
    tmp = len(rest) - 1
    
    for i in range(len(rest)) :
        answer += rest[i] * pow(3, tmp)
        tmp -= 1
        
    return answer