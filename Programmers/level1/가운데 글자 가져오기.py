def solution(s):
    if len(s) % 2 == 1 :
        return s[int(len(s)/2)]
        
    elif len(s) % 2 == 0 :
        return s[int(len(s)/2 - 1)] + s[int(len(s)/2)]