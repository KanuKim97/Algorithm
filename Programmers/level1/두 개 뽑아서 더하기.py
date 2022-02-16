def solution(numbers):
    answer = []
    
    for i in range(len(numbers)) :
        for j in range(i+1, len(numbers)):
            numberAdd = numbers[i] + numbers[j]
            
            if numberAdd not in answer :
                answer.append(numberAdd)
                answer.sort()

    return answer