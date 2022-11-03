import math

def solution(denum1, num1, denum2, num2):
    answer = []
    
    denum_final = denum1 * num2 + denum2 * num1 
    num_final = num1* num2
    
    if math.gcd(denum_final, num_final) == 1 :
        return [denum_final, num_final]
    else :
        return [denum_final/math.gcd(denum_final, num_final), num_final/math.gcd(denum_final, num_final)]
        
    return answer