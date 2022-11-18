def solution(n):
    temp = 0
    for i in range(1, 100):
        temp = factorial(i)
        if temp > n:
            return i-1
    
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else :
        return 1