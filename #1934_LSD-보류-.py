"""
 문제
   두 자연수와 A와 B 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다.
   이런 공배수 중에서 가장 작은 수를 최소 공배수라고 한다.
   예를 들어, 6과 15의 공배수는 30,60,90등이 있으며, 최소 공배수는 30이다.

   두 자연수 A와 B가 주어졌을 때, A와 B의 최소 공배수를 구하는 프로그램을 작성하시오.

 입력 
  첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 
  둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)

 출력 
   첫째 줄부터 T개의 줄에 A와 B의 최소공배수를 입력받은 순서대로 한 줄에 하나씩 출력한다.
"""

class Range_Number_Over_Err(Exception):
        def __init__(self, msg):
                self.msg = msg
        
        def __str__(self):
                return self.msg

class is_in_Range:
        def __init__ (self, Number):
                if Number > 45000 :
                        raise Range_Number_Over_Err('범위에 벗어난 값 입니다.')
                elif Number < 1:
                        raise Range_Number_Over_Err('범위에 벗어난 값 입니다.')


def print_result(Number_A, Number_B):
    Gcd = Number_A % Number_B
    Lcm = int(Number_A * Number_B / Gcd)
    print("최대 공배수는 : {0} ".format(Gcd))
    print("최소 공배수는 : {0} ".format(Lcm))

test_Case = int(input("input your test_Case : "))

while test_Case < 1001 | test_Case > 1 :
        test_Case -= test_Case
        if test_Case == 0:
                exit
        try:
                Number_A = Number_B = 0
                Number_A = int(input("A를 입력하세요 : "))
                is_in_Range(Number_A)

                Number_B = int(input("B를 입력하세요 : "))
                is_in_Range(Number_B)

                print_result(Number_A, Number_B)

        except Range_Number_Over_Err as e:
                print(e)

"""
try:
        Number_A = int(input("A를 입력하세요 : "))
        is_in_Range(Number_A)

        Number_B = int(input("B를 입력하세요 : "))
        is_in_Range(Number_B)

        print_result(Number_A, Number_B)

except Range_Number_Over_Err as e:
        print(e)
"""
