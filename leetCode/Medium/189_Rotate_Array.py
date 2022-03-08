class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums.reverse()
        n = k % len(nums) 
        
        for i in range(0, n):
            if n-i-1 < i or i == n-i-1:
                break
            nums[i], nums[n-i-1] = nums[n-i-1], nums[i]
            
        for i in range(n, len(nums)):
            if len(nums)-1-(i-n) < i or i == len(nums)-1-(i-n):
                break
            nums[i], nums[len(nums)-1-(i-n)] = nums[len(nums)-1-(i-n)], nums[i]