import re

def solution(my_string):
    answer = 0
    number = re.findall(r'\d', my_string)
    
    for i in number:
        answer += int(i)
    
    return answer