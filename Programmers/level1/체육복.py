def solution(n, lost, reserve):
    answer = n-len(lost)
    same = []
    
    
    for i in range(len(lost)):
        if lost[i] in reserve:
            same.append(lost[i])
    answer += len(same)
    
    for i in range(len(same)):
        if same[i] in reserve and same[i] in lost:
            reserve.remove(same[i])
            lost.remove(same[i])
    
    for i in range(len(lost)):
        max_Size = lost[i] + 1
        min_Size = lost[i] - 1
        
        if max_Size not in reserve and min_Size not in reserve:
            return answer
        if len(reserve) == 0:
            return answer
        if max_Size in reserve:
            reserve.remove(max_Size)
            answer += 1
            continue
        if min_Size in reserve:
            reserve.remove(min_Size)
            answer += 1
        
    return answer

    ## 65.0 점