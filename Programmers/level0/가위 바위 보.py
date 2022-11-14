def solution(rsp):
    rock = '0'
    sissor = '2'
    paper = '5'
    
    answer = ''
    
    for i in range(len(rsp)):
        if rsp[i] == sissor:
            answer += rock
        if rsp[i] == rock:
            answer += paper
        if rsp[i] == paper:
            answer += sissor
    
    return answer