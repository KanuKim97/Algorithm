def solution(s):
    answer = []
    zeroNum = 0
    count = 0
    
    while(True):
        if s != '1':
            zeroNum += s.count("0")
            s = s.replace('0', '')
            s = str(bin(len(s))[2:])
            count += 1
        else : 
            break
    
    answer.append(count)
    answer.append(zeroNum)
    
    return answer