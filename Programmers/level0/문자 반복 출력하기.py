def solution(my_string, n):
    anslist = []
    
    for i in range(len(my_string)):
        for j in range(n):
            anslist.append(my_string[i])
    
    return ''.join(anslist) 