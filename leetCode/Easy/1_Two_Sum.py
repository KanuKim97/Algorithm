'''
Runtime : 8070ms , faster than 5.00%
Memory Usage: 15Mb, less than 76.35%
'''

#Brute Force Method
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    answer.append(i)
                    answer.append(j)
                    
        return answer