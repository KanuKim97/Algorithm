def solution(left, right):
    answer = 0
    divCount = []
    listRange = range(left, right + 1)
    
    for i in range(len(listRange)) :
        for j in range(1, listRange[i]) :
            if listRange[i] % j == 0 :
                divCount.append(j)

        divCount.append(listRange[i])

        if len(divCount) % 2 == 0:
            answer += listRange[i]
            
        else :
            answer -= listRange[i]
            
        
        divCount.clear()
            
    return answer