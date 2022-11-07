import math

def solution(n):
    div = int(math.sqrt(n))
    
    if div * div == n :
        return 1 
    else :
        return 2