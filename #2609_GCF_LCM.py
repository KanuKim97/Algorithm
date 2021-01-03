"""
 문제
    두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성 하시오

 입력 
    두 개의 자연수가 주어진다. 이 둘은 10,000 이하의 자연수이며 사이에 
    한칸의 공백이 주어진다 

 출력 
    첫 째 줄에는 입력으로 주어진 두 수의 최대 공약수를, 둘째 줄에는 입력으로 이루어진
    두 수의 최소 공배수를 출력한다.
"""

class Range_Number_Over_Err(Exception):
        def __init__(self, msg):
                self.msg = msg
        
        def __str__(self):
                return self.msg

class is_inRange:
        def __init__ (self, Number):
                if Number > 10000 :
                        raise Range_Number_Over_Err('범위에 벗어난 값 입니다.')
                elif Number < 0 :
                        raise Range_Number_Over_Err('양수의 값을 입력하시오')


def print_result(Number_A, Number_B):
    Gcd = Number_A % Number_B
    Lcm = int(Number_A * Number_B / Gcd)
    print("최대 공약수는 : {0} ".format(Gcd))
    print("최소 공배수는 : {0} ".format(Lcm))

try:
        Number_A = int(input("A를 입력하세요 : "))
        is_inRange(Number_A)

        Number_B = int(input("B를 입력하세요 : "))
        is_inRange(Number_B)
        
        print_result(Number_A, Number_B)

except Range_Number_Over_Err as e:
        print(e)
