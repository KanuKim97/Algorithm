def solution(age):
    answer = ''
    alpha = ['a','b','c','d','e','f','g','h','i','j']
    listage = list(str(age))
    
    for i in range(len(listage)):
        answer += alpha[int(listage[i])]
    
    return answer