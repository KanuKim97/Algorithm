def solution(before, after):
    bl = list(before)
    al = list(after)
    
    for i in bl:
        if i in al:
            al.remove(i)

    if len(al) == 0:
        return 1
    else :
        return 0