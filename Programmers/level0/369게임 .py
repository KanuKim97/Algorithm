def solution(order):
    answer = 0
    lo = (list(str(order)))
    for i in range(len(lo)):
        if lo[i] in "3" or lo[i] in "6" or lo[i] in "9":
            answer += 1
    
    return answer