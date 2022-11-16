def solution(hp):
    ant = [5, 3, 1]
    answer = 0
    
    for i in range(len(ant)):
        if hp == 0:
            break
        answer += hp//ant[i]
        hp %= ant[i]
        
    return answer