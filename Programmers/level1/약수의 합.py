def solution(n):
    arrCount = []
    
    for i in range(1, n+1):
        if n % i == 0:
            arrCount.append(i)
            
    return sum(arrCount)