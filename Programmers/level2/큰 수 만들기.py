def solution(number, k):
    answer = []
    
    for num in number :
        while k > 0 and answer and answer[-1] < num :
            answer.pop()
            k -= 1 
            # print('k : {} answer : {}' .format(k, answer)) 과정 확인을 위한 코드
        answer.append(num)
        # print('k : {} answer : {}' .format(k, answer)) 과정 확인을 위한 코드
    
    
    return ''.join(answer[:len(answer)-k])