def solution(num, k):
    num_str = list(str(num))
    
    if str(k) in num_str:
        return num_str.index(str(k))+1
    else :
        return -1
    