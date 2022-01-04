def solution(d, budget):
    d.sort()

    if sum(d) == budget:
        return len(d)
        
    elif sum(d) > budget :
        for i in reversed(range(len(d))) :
            d.pop(i)
            if sum(d) <= budget:
                return len(d)
                break
    else :
        return len(d)