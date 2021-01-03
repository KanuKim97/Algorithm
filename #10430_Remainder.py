"""
 문제
  (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
  (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
  세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

 입력 
  A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)

 출력 
  첫째 줄에 (A+B)%C
  둘째 줄에 ((A%C) + (B%C))%C
  셋째 줄에 (A×B)%C
  넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
"""

class Range_Number_Over_Err(Exception):
        def __init__(self, msg):
                self.msg = msg
        
        def __str__(self):
                return self.msg

class is_In_Number_Range:
        def __init__ (self, Number):
                if Number < 2 :
                        raise Range_Number_Over_Err('범위에 벗어난 값 입니다.')
                elif Number > 10000:
                        raise Range_Number_Over_Err('범위에 벗어난 값 입니다.')


def print_result(Number_A, Number_B, Number_C):
        print("{0}".format(bool( (Number_A + Number_B) % Number_C )))
        print("{0}".format(bool( ((Number_A % Number_C) + (Number_B % Number_C)) % Number_C )))
        print("{0}".format(bool((Number_A * Number_B) % Number_C)))
        print("{0}".format(bool(((Number_A % Number_C) * (Number_B % Number_C)) % Number_C )))


try:
        Number_A = int(input("A를 입력하세요 : "))
        is_In_Number_Range(Number_A)

        Number_B = int(input("B를 입력하세요 : "))
        is_In_Number_Range(Number_B)

        Number_C = int(input("C를 입력하세요 : "))
        is_In_Number_Range(Number_C)

        print_result(Number_A, Number_B, Number_C)
        
except Range_Number_Over_Err as e:
        print(e)

