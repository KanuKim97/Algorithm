def solution(my_string, num1, num2):
    temp = ''
    s = list(my_string)
    
    temp = s[num1]
    s[num1] = s[num2]
    s[num2] = temp
    
    return ''.join(s)