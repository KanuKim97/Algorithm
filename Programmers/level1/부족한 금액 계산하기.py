def solution(price, money, count):
    tmp = 0
    finalValue = 0
    
    for i in range(1, count+1):
        tmp += price*i
        finalValue = tmp-money
    
    if finalValue <= 0:
        return 0
        
    return finalValue