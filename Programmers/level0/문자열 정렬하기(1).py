def solution(my_string):
    answer = []
    
    for i in range(len(my_string)):
        if my_string[i].isdecimal():
            answer.append(int(my_string[i]))
    
    answer.sort()
    return answer