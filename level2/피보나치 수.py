def solution(n):
    answer = 0
    next = 1
    
    for i in range(n):
        answer, next = next, answer+next
        
    return answer%1234567