class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        localMax = 0
        globalMax = nums[0]
        
        if len(nums) == 1 :
            return max(nums)
        else :
            for i in range(len(nums)):
                localMax = max(nums[i], localMax+nums[i])
                
                if localMax > globalMax :
                    globalMax = localMax
                
        return globalMax