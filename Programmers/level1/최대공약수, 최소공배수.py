# math.lcm()은 Python 3.9 Version 에서 사용가능 
# Programmers는 3.8.5 Version 이므로 lcm() 사용 불가 
import math 

def solution(n, m):
    answer = []

    answer.append(math.gcd(n,m))
    answer.append(n * m / math.gcd(n,m))

    return answer

