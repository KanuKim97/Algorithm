'''
Wrong answer 

Input : [3,3,3], 3

Output : [0,1]

Expected : [0,2]
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        answer = []
        first_idx, last_idx  = 0, len(nums)
        
        if target in nums :
            first_idx = nums.index(target)
            answer.append(first_idx)
            
            while True :
                mid = (first_idx + last_idx) // 2
                
                if target == nums[mid]:
                    answer.append(mid)
                    break
                else :
                    last_idx = mid
                
        else : 
            answer.append(-1)
            answer.append(-1)
        
        
        return answer