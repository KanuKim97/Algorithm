class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        if target in nums : 
            return nums.index(target)
        else :
            while left <= right :
                mid = (left + right) // 2
                
                if nums[mid] > target :
                    right = mid - 1
                else : 
                    left = mid + 1
                
            return left