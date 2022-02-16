import math

def solution(arr):
    answer = arr[0]
    
    for i in arr :
        answer = i * answer // math.gcd(i, answer)
        
    return answer