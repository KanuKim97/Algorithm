def solution(s):
    stack_1 = []
    list_String = list(s)
    
    for i in range(len(list_String)):
        if list_String[i] == '(':
            stack_1.append(list_String[i])
            
        else :
            if len(stack_1) == 0 :
                stack_1.append(list_String[i])
            else :
                stack_1.pop()
    
    if len(stack_1) != 0 :
        return False
    else :
        return True