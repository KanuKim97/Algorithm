def solution(n):
    L = list(map(int, str(n)))
    answer = []
    
    for i in reversed(range(len(L))):
        answer.append(L[i])
    
    return answer