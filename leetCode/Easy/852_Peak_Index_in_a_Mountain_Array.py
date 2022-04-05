class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)
        
        if len(arr) < 3 :
            return -1 
        else :
            while True :
                mid = (left + right) // 2
                
                if arr[mid] > arr[mid-1] and arr[mid+1] < arr[mid]  :
                    return mid 
                elif arr[mid] < arr[mid+1] :
                    left = mid + 1
                else :
                    right = mid - 1 