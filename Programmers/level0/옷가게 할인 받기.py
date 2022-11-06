def solution(price):
    if price >= 500000: 
        price *= 0.8
        return int(price)
    if price >= 300000: 
        price *= 0.9
        return int(price)
    if price >= 100000: 
        price *= 0.95
        return int(price)
    else :
        return price