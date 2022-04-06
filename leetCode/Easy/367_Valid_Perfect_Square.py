class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        row = num**(1/2) 
        
        if int(row) * int(row) == num : 
            return True
        else :
            return False