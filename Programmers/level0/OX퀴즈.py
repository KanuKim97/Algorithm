def solution(quiz):
    answer = []
    
    for i in range(len(quiz)):
        str1 = list(quiz[i])
        if int(eval(''.join(list(str1)[:list(str1).index('=')]))) == int(''.join(list(str1)[list(str1).index('=')+1:])):
            answer.append('O')
        else :
            answer.append('X')
            
    return answer