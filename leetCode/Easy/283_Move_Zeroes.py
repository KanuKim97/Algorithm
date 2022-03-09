class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index_number = 0
        
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[index_number] = nums[i]
                index_number += 1
        
        for i in range(index_number, len(nums)):
            nums[i] = 0
        