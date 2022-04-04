# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        
        while True :
            mid_num = (left + right) // 2
            
            if guess(mid_num) == 1 :
                left = mid_num + 1
            elif guess(mid_num) == -1 :
                right = mid_num - 1 
            else :
                return mid_num