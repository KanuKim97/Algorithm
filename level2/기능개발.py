import math

def solution(progresses, speeds):
    answer = []
    low = []
    
    for i in range(len(progresses)) :
        rest = 100 - progresses[i]
        low.append(math.ceil(rest/speeds[i]))
    
    for i in range(len(low)):
        org = low[i]
        cnt = 1
        
        if low[i] == 0 :
            continue
            
        for j in range(i+1, len(low)):
            cmp = low[j]
            if org >= cmp :
                cnt += 1
                low[j] = 0
            else : 
                break
        answer.append(cnt)
    return answer