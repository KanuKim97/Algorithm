def solution(sides):
    
    if sides.pop(sides.index(max(sides))) >= sum(sides): 
        return 2 
    
    return 1 