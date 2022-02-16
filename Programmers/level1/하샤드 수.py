def solution(x):
    xList = list(map(int, str(x)))
    if x % sum(xList) == 0:
        return True
    else :
        return False