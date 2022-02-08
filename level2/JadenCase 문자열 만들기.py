def solution(s):
    tmp = []
    s = s.lower()
    listA = s.split(' ')
    
    for i in range(len(listA)) :
        if listA[i].islower() :
            tmp.append(listA[i][0].upper() + listA[i][1:]) 
        else :
            tmp.append(listA[i])  
    
    return ' '.join(tmp)