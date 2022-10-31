def solution(arr):
    answer = []
    j = -1
    
    for i in range(len(arr)):
        if arr[i] == j:
            j = arr[i]
            
        else :
            j = arr[i]
            answer.append(j)
            
    return answer